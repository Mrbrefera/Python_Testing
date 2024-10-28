from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    def on_start(self):
        """This will be executed once per user at the start of the test."""
        self.email = "user@example.com"  # Remplace par un email existant dans clubs.json si possible

    @task(1)
    def index(self):
        """Test the homepage (index route)."""
        self.client.get("/")

    @task(2)
    def login(self):
        """Test the login route."""
        response = self.client.post("/showSummary", data={"email": self.email})
        if "welcome.html" not in response.text:
            response.failure("Failed to log in with provided email.")

    @task(3)
    def book(self):
        """Test booking route with known competition and club."""
        # Replace Sample Competition and Sample Club with actual values in competitions and clubs
        competition_name = "Sample Competition"
        club_name = "Sample Club"
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        if "booking.html" not in response.text:
            response.failure("Failed to access booking page for competition.")

    @task(4)
    def purchase_places(self):
        """Test purchasing places after booking."""
        # Replace Sample Competition and Sample Club with actual values in competitions and clubs
        competition_name = "Sample Competition"
        club_name = "Sample Club"
        response = self.client.post("/purchasePlaces", data={
            "competition": competition_name,
            "club": club_name,
            "places": 1
        })
        if "Great - booking complete!" not in response.text:
            response.failure("Failed to complete booking.")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
