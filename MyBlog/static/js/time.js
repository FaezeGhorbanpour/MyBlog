
    var months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
                'Jul':7,'Aug':8,'Sep':9,'Sept':9,'Oct':10,'Nov':11,'Dec':12};
    var new_months={1:'فروردین',2:'اردیبهشت',3:'خرداد',4:'تیر',5:'مرداد',6:'شهریور',
                7:'مهر',8:'آبان',9:'آذر',10:'دی',11:'بهمن',12:'اسفند'};

function convertDate(input) {

    var fields = input.split(' ');
    var mon = months[fields[1]];
    var day,new_day,new_mon;
    if (fields[2] == "") {
        var year = fields[5];
        var d = fields[3];
    }
    else{
        var year = fields[4];
        var d = fields[2];
    }
    var flag2 = 0;
    if(((year)%100 == 0 && (year)%400 == 0) || ((year)%100 != 0 && (year)%4 == 0))
        flag2 = 1;
    var flag = 10;
    if(((year-1)%100 == 0 && (year-1)%400 == 0) || ((year-1)%100 != 0 && (year-1)%4 == 0))
        flag = 11;
    if (mon <= 2) day = (mon-1) * 31 + parseInt(d);
    else if (mon == 3) day = 31 + 28 + (flag2) +  parseInt(d);
    else if(mon == 4 ) day = 31 * 2 + 28 + (flag2) +  parseInt(d);
    else if (mon == 5)day = 30 + 2*31 + 28 + (flag2) +  parseInt(d);
    else if(mon == 6)day = 3*31 + 30 +28 + (flag2) +  parseInt(d);
    else if(mon == 7)day = 2*30+3*31+28 + (flag2) +  parseInt(d);
    else if(mon == 8)day = 4*31 + 2*30 + 28 + (flag2) +  parseInt(d);
    else if(mon == 9)day = 5*31 + 2*30 + 28 + (flag2) +  parseInt(d);
    else if(mon == 10)day = 5*31 + 3*30 +28 + (flag2) +  parseInt(d);
    else if(mon == 11)day = 6*31 + 3*30 + 28 + (flag2) +  parseInt(d);
    else day = 6*31 +  4*30 + 28 + (flag2) +  parseInt(d);;


    var new_year;
    var temp,temp2,temp3,temp4;
    if (day <= 79) {
        new_year = year - 622;

        temp = flag + day;
        temp2 = Math.floor(temp / 30);
        temp3 = temp % 30;
        if(temp3 == 0){
            new_mon = temp2 + 9;
            new_day = 30;
        }
        else {
            new_mon = temp2 + 10;
            new_day = temp3;
        }
    }
    else {
        new_year = year - 621;
        temp = day - 79;
        if (temp < 186){
            temp2 = Math.floor(temp / 31);
            temp3 = temp % 31;
            if(temp3 == 0)
            {
                new_mon = temp2;
                new_day = 31;
            }
            else {
                new_mon = temp2+1;
                new_day=temp3
            }
        }
        else {
             temp2 = day - 186;
             temp3 = Math.floor(temp2 / 30);
             temp4 = temp2 % 30;
            if (temp4 == 0) {
                new_mon = temp3 + 6;
                new_day = 30;
            }
            else {
                new_mon = temp3 + 7;
                new_day = temp4;
            }
        }
    }
return (new_year + " : " + new_months[new_mon] + " : " + new_day );
}
