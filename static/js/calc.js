$(document).ready(function () {
    field = $(".main-field")[0].children[0];
    mValue = "0";
    clearField = function(){
        dotAvalable = true;
        mValue = "0";
        field.value = mValue;
    }
    clearField();

    // Обработка цифр и точки
    $(".number").on('click', function(event) {
        if (mValue=="0"){
            mValue = $(this).data("number");
        }
        else{
            mValue = field.value + $(this).data("number");
        }
        field.value = mValue
        hideError();
    });
   // Обработка символов
    $(".symbol").on('click', function(event) {
        sym = $(this).data("symbol")
        switch(sym){
            case "c":
                clearField();
                break;
            case ".":
                if (dotAvalable){
                    mValue += sym;
                    dotAvalable = false;
                }
                break;
            case "=":
                $.get(
                    "do-calc",
                    {"field": mValue},
                    response
                );
                break;
            case ")":
                if (/[\d\+*\)(-]+\d+$/.test(mValue)){
                    mValue += sym;
                }
                break;
            case "(":
                if (/[\d\+*\)(-]+[\+*(-]$/.test(mValue)){
                    mValue += sym;
                }
                break;
            case "←":
                mValue = mValue.substring(0, mValue.length-1);
                break;
            default:
                mValue += sym;
        }
        hideError();
        field.value = mValue;
    });

    hideError = function(){
        errItem = $("#ev-error")[0];
        if (errItem.className.indexOf("hidden") < 0){
            errItem.className += " hidden";
        }
    }

    response = function(r){
        field.value = mValue = r.value;
        if (r.errorMsg!= ""){
            errItem = $("#ev-error")[0];
            errItem.children[0].textContent = r.errorMsg;
            errItem.className = errItem.className.replace("hidden", "");
        }
    }

});

