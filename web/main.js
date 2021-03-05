var buttons = document.getElementsByClassName("cl");
var angle = document.getElementById("angle");
var rt = document.getElementById("RT");
var  ft = document.getElementById("FI");
var mv = document.getElementById("move");
var servo_id = 1;
mv.addEventListener('click', move)

for (let btn of buttons){
   btn.addEventListener('click', lock_servo);

}
function lock_servo(e){
    servo_id =parseInt(e.target.id);
}
eel.expose(move);
async function move(){
    let x = await eel.main(servo_id,parseInt(angle.value),parseInt(rt.value),parseInt(ft.value))();
}

// eel.expsoe_function(getServo)
// function getServo(){
// return servo_id
// }
// eel.expose_function(getAngle)
// function getAngle(){
//     return angle.value;
// }
// eel.expose_function(getRt)
// function getRt(){
//     return rt.value
// }
// eel.expose_function(getRi)
// function getRi(){
//     return fi.value
// }