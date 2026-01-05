#!/usr/bin/env python3
"""
TikTok Auto-Upload Module
Handles OAuth authentication and video upload to TikTok via Content Posting API
"""

import os
import json
import requests
import time
from datetime import datetime
from typing import Dict, Optional
from urllib.parse import urlencode
import webbrowser

class TikTokUploader:
    def __init__(self, client_key: str, client_secret: str):
        """
        Initialize TikTok Uploader with API credentials
        
        Args:
            client_key: Your TikTok App Client Key
            client_secret: Your TikTok App Client Secret
        """
        self.client_key = client_key
        self.client_secret = client_secret
        self.redirect_uri = "http://localhost:8000/callback"
        self.access_token = None
        self.open_id = None
        
        # TikTok API endpoints
        self.auth_url = "https://www.tiktok.com/v2/auth/authorize/"
        self.token_url = "https://open.tiktokapis.com/v2/oauth/token/"
        self.upload_init_url = "https://open.tiktokapis.com/v2/post/publish/inbox/video/init/"
        self.upload_url = "https://open.tiktokapis.com/v2/post/publish/video/init/"
        
    def get_authorization_url(self) -> str:
        """
        Generate OAuth authorization URL for user to grant permissions
        
        Returns:
            Authorization URL string
        """
        params = {
            "client_key": self.client_key,
            "scope": "user.info.basic,video.upload,video.publish",
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "state": "tiktok_oauth_state"
        }
        
        auth_url = f"{self.auth_url}?{urlencode(params)}"
        print(f"\n🔐 Opening authorization URL in browser...")
        print(f"If it doesn't open automatically, visit: {auth_url}")
        
        return auth_url
    
    def authorize(self) -> bool:
        """
        Start OAuth flow and get access token
        
        Returns:
            True if authorization successful
        """
        # Step 1: Get authorization URL
        auth_url = self.get_authorization_url()
        
        # Open browser for user to authorize
        try:
            webbrowser.open(auth_url)
        except:
            print("Could not open browser automatically. Please open the URL manually.")
        
        # Step 2: User manually enters authorization code
        print("\n📋 After authorizing, you'll be redirected to a URL.")
        print("Copy the 'code' parameter from the URL and paste it here:")
        auth_code = input("Authorization code: ").strip()
        
        # Step 3: Exchange code for access token
        return self.get_access_token(auth_code)
    
    def get_access_token(self, auth_code: str) -> bool:
        """
        Exchange authorization code for access token
        
        Args:
            auth_code: Authorization code from OAuth callback
            
        Returns:
            True if token obtained successfully
        """
        data = {
            "client_key": self.client_key,
            "client_secret": self.client_secret,
            "code": auth_code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri
        }
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache"
        }
        
        try:
            response = requests.post(self.token_url, data=data, headers=headers)
            response.raise_for_status()
            
            token_data = response.json()
            
            if "data" in token_data:
                self.access_token = token_data["data"]["access_token"]
                self.open_id = token_data["data"]["open_id"]
                
                # Save tokens for future use
                self._save_tokens(token_data["data"])
                
                print("✅ Authorization successful!")
                print(f"Access token obtained for user: {self.open_id}")
                return True
            else:
                print(f"❌ Error getting access token: {token_data}")
                return False
                
        except Exception as e:
            print(f"❌ Authorization failed: {e}")
            return False
    
    def _save_tokens(self, token_data: Dict):
        """Save tokens to file for reuse"""
        with open("tiktok_tokens.json", "w") as f:
            json.dump(token_data, f, indent=2)
        print("💾 Tokens saved to tiktok_tokens.json")
    
    def load_tokens(self) -> bool:
        """
        Load saved tokens from file
        
        Returns:
            True if tokens loaded successfully
        """
        try:
            with open("tiktok_tokens.json", "r") as f:
                token_data = json.load(f)
                self.access_token = token_data.get("access_token")
                self.open_id = token_data.get("open_id")
                
                if self.access_token and self.open_id:
                    print("✅ Loaded saved tokens")
                    return True
                return False
        except FileNotFoundError:
            print("⚠️  No saved tokens found. Please authorize first.")
            return False
    
    def upload_video(self, video_path: str, title: str, 
                     description: str = "", 
                     privacy_level: str = "PUBLIC_TO_EVERYONE",
                     disable_duet: bool = False,
                     disable_comment: bool = False,
                     disable_stitch: bool = False) -> Optional[Dict]:
        """
        Upload video to TikTok
        
        Args:
            video_path: Path to video file
            title: Video title/caption
            description: Video description (optional)
            privacy_level: Privacy setting (PUBLIC_TO_EVERYONE, MUTUAL_FOLLOW_FRIENDS, etc.)
            disable_duet: Disable duet feature
            disable_comment: Disable comments
            disable_stitch: Disable stitch feature
            
        Returns:
            Upload response data or None if failed
        """
        if not self.access_token:
            print("❌ Not authorized. Please run authorize() first.")
            return None
        
        # Step 1: Initialize upload
        print(f"\n📤 Initializing upload for: {os.path.basename(video_path)}")
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json; charset=UTF-8"
        }
        
        # Get video file info
        video_size = os.path.getsize(video_path)
        
        init_data = {
            "post_info": {
                "title": title,
                "description": description,
                "privacy_level": privacy_level,
                "disable_duet": disable_duet,
                "disable_comment": disable_comment,
                "disable_stitch": disable_stitch
            },
            "source_info": {
                "source": "FILE_UPLOAD",
                "video_size": video_size,
                "chunk_size": video_size,  # Upload in one chunk
                "total_chunk_count": 1
            }
        }
        
        try:
            # Initialize upload
            response = requests.post(self.upload_init_url, 
                                    headers=headers, 
                                    json=init_data)
            response.raise_for_status()
            
            init_result = response.json()
            
            if init_result.get("error"):
                print(f"❌ Upload initialization failed: {init_result['error']}")
                return None
            
            upload_url = init_result["data"]["upload_url"]
            publish_id = init_result["data"]["publish_id"]
            
            print(f"✅ Upload initialized. Publish ID: {publish_id}")
            
            # Step 2: Upload video file
            print("⬆️  Uploading video file...")
            
            with open(video_path, "rb") as video_file:
                video_data = video_file.read()
                
            upload_headers = {
                "Content-Type": "video/mp4",
                "Content-Length": str(video_size)
            }
            
            upload_response = requests.put(upload_url, 
                                          headers=upload_headers, 
                                          data=video_data)
            upload_response.raise_for_status()
            
            print("✅ Video uploaded successfully!")
            print(f"📊 Publish ID: {publish_id}")
            print(f"⏰ Video will be processed and published shortly.")
            
            return {
                "publish_id": publish_id,
                "status": "processing",
                "title": title,
                "uploaded_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"❌ Upload failed: {e}")
            return None
    
    def check_upload_status(self, publish_id: str) -> Optional[Dict]:
        """
        Check status of uploaded video
        
        Args:
            publish_id: Publish ID from upload_video()
            
        Returns:
            Status data or None
        """
        if not self.access_token:
            print("❌ Not authorized")
            return None
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        params = {"publish_id": publish_id}
        
        try:
            response = requests.post(
                "https://open.tiktokapis.com/v2/post/publish/status/fetch/",
                headers=headers,
                json=params
            )
            response.raise_for_status()
            
            status_data = response.json()
            return status_data.get("data")
            
        except Exception as e:
            print(f"❌ Status check failed: {e}")
            return None


def main():
    """
    Example usage of TikTok Uploader
    """
    print("="*60)
    print("   TikTok Auto-Uploader")
    print("   Upload videos automatically to TikTok")
    print("="*60)
    
    # Get credentials from environment
    client_key = os.getenv('TIKTOK_CLIENT_KEY')
    client_secret = os.getenv('TIKTOK_CLIENT_SECRET')
    
    if not client_key or not client_secret:
        print("\n❌ Missing TikTok API credentials!")
        print("\nPlease set environment variables:")
        print("export TIKTOK_CLIENT_KEY='your-client-key'")
        print("export TIKTOK_CLIENT_SECRET='your-client-secret'")
        print("\nGet these from: https://developers.tiktok.com/apps")
        return
    
    uploader = TikTokUploader(client_key, client_secret)
    
    # Try to load saved tokens first
    if not uploader.load_tokens():
        # First time: need to authorize
        print("\n🔐 First time setup: Authorization required")
        if not uploader.authorize():
            print("❌ Authorization failed. Exiting.")
            return
    
    # Example: Upload a video
    print("\n📹 Ready to upload videos!")
    print("\nExample usage:")
    print('uploader.upload_video("video.mp4", "Check out this amazing hack! #tiktokmademebuyit")')

if __name__ == "__main__":
    main()
