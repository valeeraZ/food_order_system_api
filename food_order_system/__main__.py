import uvicorn

from food_order_system.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "food_order_system.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
