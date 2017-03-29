 $(document).ready(function () {
    $('#chair_creation').click(function(){
        var name=$("#name").val()
        var age=$("#age").val()
        var sex=$("#sex").val()
        var weight=$("#weight").val()
        var height=$("#height").val()
        console.log(name)
        console.log(age)
        console.log(sex)
        console.log(weight)
        console.log(height)
        if(name!='' && age!='' && weight!='' && height!=''){
            $('#information1').hide()
            $('#information2').show()
            document.getElementById('person_name').innerHTML=name;
            document.getElementById('name1').innerHTML=name;
            document.getElementById('sex1').innerHTML=sex;
            document.getElementById('age1').innerHTML=age;
            document.getElementById('weight1').innerHTML=weight;
            document.getElementById('height1').innerHTML=height;
            $('#result').show()
            $('#threeD').show()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair1').show()
            // if(weight>0 && weight<=20){
            //     document.getElementById('person_name').innerHTML=name;
                
            // }
            // else if(weight>20 && weight<=40){
            //     document.getElementById('person_name').innerHTML=name;
            //     $('#chair1').hide()
            //     $('#chair3').hide()
            //     $('#chair4').hide()
            //     $('#chair2').show()
            // }
            // else if(weight>40 && weight<=60){
            //     document.getElementById('person_name').innerHTML=name;
            //     $('#chair1').hide()
            //     $('#chair2').hide()
            //     $('#chair4').hide()
            //     $('#chair3').show()
            // }
            // else if(weight>60 && weight<=2000){
            //     document.getElementById('person_name').innerHTML=name;
            //     $('#chair1').hide()
            //     $('#chair2').hide()
            //     $('#chair3').hide()
            //     $('#chair4').show()
            // }
        }
        else{
            swal({
                    title: "Please Fill Up Mssing Information.",
                    type: "warning",
                    confirmButtonText: "OK"
                })
        }
    });

    $('#plus').click(function(){
       var number = Math.floor(Math.random() * 4) + 1;
       console.log(number)
       if(number==1){
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair2').show()
       }
       else if(number==2){
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair3').show()
       }
       else if(number==3){
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair4').show()
       }
       else{
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair1').show()
       }
    });
    $('#minus').click(function(){
       var number = Math.floor(Math.random() * 4) + 1;
       console.log(number)
       if(number==1){
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair4').show()
       }
       else if(number==2){
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair1').show()
       }
       else if(number==3){
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair2').show()
       }
       else{
            $('#chair1').hide()
            $('#chair2').hide()
            $('#chair3').hide()
            $('#chair4').hide()
            $('#chair3').show()
       }
    });

    $('#submit').click(function(){
    swal({
            title: "Information Submitted Successfully.",
            type: "success",
            confirmButtonText: "OK"
            }).then(function () {
            window.location = "index.html";
        });
    });

    $('#cancel').click(function(){
        window.location = "create_new_chair.html";
    });
});