import threading
import time

import pygame

image = pygame.image.load("01_image.png")
background = pygame.image.load("background.png")
image.set_colorkey((255, 0, 255))
image.set_alpha(128)


# 메인 함수 정의
def main():
    # 파이게임 모듈 초기화
    pygame.init()
    # 로고 로드하고 세팅
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # 스크린 사이즈
    screen_width = 240
    screen_height = 180

    # 스마일의 위치 값 정의
    xpos = 50
    ypos = 50
    # 각 프레임 별로 얼마나 움직일 지 정함
    step_x = 10
    step_y = 10

    # 240 x 180 사이즈의 스크린 화면을 만듦
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.blit(background, (0, 0))
    screen.blit(image, (xpos, ypos))
    pygame.display.flip()

    # 메인 루프를 제어할 변수 정의
    running = True

    # 메인 루프
    while running:
        # 스마일이 스크린에 있는지, 방향이 변하지 않는지 체크한다.
        if xpos > screen_width - 64 or xpos < 0:
            step_x = -step_x
        if ypos > screen_height - 64 or ypos < 0:
            step_y = -step_y
        # 스마일의 위치 값을 업데이트한다.
        xpos += step_x
        ypos += step_y

        # 화면을 지운다. (화면을 배경화면을 덮음)
        screen.blit(background, (0, 0))
        # 그 다음 스마일을 블리팅한다.
        screen.blit(image, (xpos, ypos))
        # 그리고 스크린을 업데이트 한다.
        pygame.display.flip()
        # 파이게임을 지정한 시간 만큼 멈춘다.
        pygame.time.wait(1000)

        # 이벤트 핸들러, 이벤트 큐로부터 모든 이벤트를 얻는다.
        for event in pygame.event.get():
            # QUIT 타입의 이벤트라면 다음 코딩을 실행
            if event.type == pygame.QUIT:
                # 메인 루프를 탈출하기 위해 변수를 False 로 바꾼다.
                running = False


# 현재 모듈이 메인 스크립트라면 메인 함수 실행
# (이 모듈을 임포트하면 아무것도 실행하지 않는다)
if __name__ == "__main__":
    # call the main function
    main()
