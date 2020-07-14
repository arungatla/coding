# balloon burst

def balloonBurst(balloons):
    balloons.insert(0,1)
    balloons.append(1)

    print(balloons)

balloonBurst([1,2,3,4])