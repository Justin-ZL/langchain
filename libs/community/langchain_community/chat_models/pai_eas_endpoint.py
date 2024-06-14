
def _call_eas(self, query_body: dict) -> Any:
    """Generate text from the eas service."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"{self.eas_service_token}",
    }

    # make request
    response = requests.post(
        self.eas_service_url, headers=headers, json=query_body, timeout=self.timeout
    )

    if response.status_code != 200:
        raise Exception(
            f"Request failed with status code {response.status_code}"
            f" and message {response.text}"
        )

    return response.content  # This should return response.content to match the bytes type requirement
        return response.content
