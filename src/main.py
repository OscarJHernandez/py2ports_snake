import pygame

WIDTH = 640
HEIGHT = 480
FPS = 60


def main() -> None:
    pygame.init()

    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    x = WIDTH // 2
    y = HEIGHT // 2
    speed = 4
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button in (6, 9, 10):
                    running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed

        if joystick:
            hx, hy = joystick.get_hat(0)
            x += hx * speed
            y -= hy * speed

        screen.fill((20, 20, 30))
        pygame.draw.rect(screen, (230, 230, 100), (x, y, 24, 24))
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        raise
