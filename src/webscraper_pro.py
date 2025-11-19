#!/usr/bin/env python3
"""
WebScraper Pro - Advanced web scraping tool with proxy support.
"""

import urllib.request
from urllib.parse import urljoin, urlparse
from typing import List, Optional

class WebScraper:
    """Web scraper with proxy support."""
    def __init__(self, proxy: Optional[str] = None):
        self.proxy = proxy
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (WebScraper Pro)'
        }
    
    def fetch(self, url: str) -> Optional[str]:
        """Fetch content from URL."""
        try:
            req = urllib.request.Request(url, headers=self.headers)
            
            if self.proxy:
                proxy_handler = urllib.request.ProxyHandler({'http': self.proxy, 'https': self.proxy})
                opener = urllib.request.build_opener(proxy_handler)
            else:
                opener = urllib.request.build_opener()
            
            with opener.open(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_links(self, html: str, base_url: str) -> List[str]:
        """Extract all links from HTML."""
        import re
        pattern = r'href=["\']([^"\']+)["\']'
        links = re.findall(pattern, html)
        return [urljoin(base_url, link) for link in links]

if __name__ == "__main__":
    scraper = WebScraper()
    print("WebScraper Pro initialized")
