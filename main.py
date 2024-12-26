cuteBot.singleheadlights(cuteBot.RGBLights.RGB_L, 0, 0, 0)

def on_forever():
    if cuteBot.IR_Button(cuteBot.IRButtons.UP):
        cuteBot.stopcar()
basic.forever(on_forever)
