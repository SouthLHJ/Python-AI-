class Rabbit : 
    # 토끼 클래스의 속성(변수)
    shape = '🐇'
    xPos,yPos = 0,0

    # 토끼 클래스의 행동 ( 메서드 )
    # self를 첫 번째 매개변수로 꼭 정의해야 함
    def goto(self,x,y): # 토끼를 주어진 좌표로 이동
        self.xPos = x # 클래스의 속성 xPos를 주어진 x로 설정
        self.yPos = y
    