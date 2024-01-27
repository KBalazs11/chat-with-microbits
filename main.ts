radio.setGroup(1)
input.onButtonPressed(Button.A, function() {
    radio.sendString("Your text")
})
radio.onReceivedString(function (ReceivedString) {
    basic.showString(ReceivedString)
})
radio.setGroup(1)
input.onButtonPressed(Button.B, function () {
    radio.sendString("Your text")
})
radio.onReceivedString(function (ReceivedString) {
    basic.showString(ReceivedString)
})