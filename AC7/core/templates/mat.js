
var apCont = 0;
var rpCont = 0;


function soma(value) {
    if (value == "Aprovado") {
        apCont ++;
        console.log('ap',apCont)
    } else{
        rpCont ++;
        console.log('rp', rpCont)
    }
       
}


function validateForm() {
    if(apCont >= 20 && apCont <= 60){
        confirm('Aprovados: '+ apCont + ' Cancelados: ' + rpCont,'.');
    } else {
        alert('Minimo: 20, Maximo: 60')
    }
}