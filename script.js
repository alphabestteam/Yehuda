/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/

const d = new Date();

function starSign(date){
    month = date.getMonth()+1
    day = date.getDate()

    switch (month) {
        case 1:
            if (day >= 21) return "Aquarius";
            if (day <= 20) return "Capricorn";
            break;
        case 2:
            if (day >= 20) return "Pisces";
            if (day <= 19) return "Aquarius";
            break;
        case 3:
            if (day >= 21) return "Aries";
            if (day <= 20) return "Pisces";
            break;
        case 4:
            if (day >= 21) return "Taurus";
            if (day <= 20) return "Aries";
            break;
        case 5:
            if (day >= 22) return "Gemini";
            if (day <= 21) return "Taurus";
            break;
        case 6:
            if (day >= 22) return "Cancer";
            if (day <= 22) return "Gemini";
            break;
        case 7:
            if (day >= 23) return "Leo";
            if (day <= 23) return "Cancer";
            break;
        case 8:
            if (day >= 24) return "Virgo";
            if (day <= 23) return "Leo";
            break;
        case 9:
            if (day >= 24) return "Libra";
            if (day <= 23) return "Virgo";
            break;
        case 10:
            if (day >= 24) return "Scorpio";
            if (day <= 22) return "Libra";
            break;
        case 11:
            if (day >= 23) return "Sagittarius";
            if (day <= 21) return "Scorpio";
            break;
        case 12:
            if (day >= 22) return "Capricorn";
            if (day <= 20) return "Sagittarius";
            break;
        default:
            return "Not a valid date";
    }
}
alert(starSign(d));