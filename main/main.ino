int led = 7;
int mm = 0;


void setup(){
    pinMode(led, OUTPUT);
    Serial.begin(9600);
}

void esp_letra(){
    delay(700);
}

void esp_palabra(){
    delay(1750);
}

void punto(){
    digitalWrite(led, 1);
    delay(50);
    digitalWrite(led, 0);
    delay(300);
}

void raya(){
    digitalWrite(led, 1);
    delay(350);
    digitalWrite(led, 0);
    delay(250);
}


void loop(){
    if (Serial.available() > 0){
        mm = Serial.read();
        ineterprete(mm);
    }
}

void a(){
    punto();
    raya();
}

void b(){
    raya();
    punto();
    punto();
    punto();
}

void c(){
    raya();
    punto();
    raya();
    punto();
}

void d(){
    raya();
    punto();
    punto();
}

void e(){
    punto();
}

void f(){
    punto();
    punto();
    raya();
    punto();
}

void g(){
    raya();
    raya();
    punto();
}

void h(){
    punto();
    punto();
    punto();
    punto();
}

void i(){
    punto();
    punto();
}

void j(){
    punto();
    raya();
    raya();
    raya();
}

void k(){
    raya();
    punto();
    raya();
}

void l(){
    punto();
    raya();
    punto();
    punto();
}

void m(){
    raya();
    raya();
}

void n(){
    raya();
    punto();
}

void o(){
    raya();
    raya();
    raya();
}

void p(){
    punto();
    raya();
    raya();
    punto();
}

void q(){
    raya();
    raya();
    punto();
    raya();
}

void r(){
    punto();
    raya();
    punto();
}

void s(){
    punto();
    punto();
    punto();
}

void t(){
    raya();
}

void u(){
    punto();
    punto();
    raya();
}

void v(){
    punto();
    punto();
    punto();
    raya();
}

void w(){
    punto();
    raya();
    raya();
}

void x(){
    raya();
    punto();
    punto();
    raya();   
}

void y(){
    raya();
    punto();
    raya();
    raya();
}

void z(){
    raya();
    raya();
    punto();
    punto();
}

void uno(){
    punto();
    raya();
    raya();
    raya();
    raya();
}

void dos(){
    punto();
    punto();
    raya();
    raya();
    raya();
}

void tres(){
    punto();
    punto();
    punto();
    raya();
    raya();
}

void cuatro(){
    punto();
    punto();
    punto();
    punto();
    raya();
}

void cinco(){
    punto();
    punto();
    punto();
    punto();
    punto();
}

void seis(){
    raya();
    punto();
    punto();
    punto();
    punto();
}

void siete(){
    raya();
    raya();
    punto();
    punto();
    punto();
}

void ocho(){
    raya();
    raya();
    raya();
    punto();
    punto();
}

void nueve(){
    raya();
    raya();
    raya();
    raya();
    punto();
}

void cero(){
    raya();
    raya();
    raya();
    raya();
    raya();
}


void ineterprete(int men){
    switch(men){
        case 'a':
            a();
            esp_letra();
            break;
        case 'b':
            b();
            esp_letra();
            break;
        case 'c':
            c();
            esp_letra();
            break;
        case 'd':
            d();
            esp_letra();
            break;
        case 'e':
            e();
            esp_letra();
            break;
        case 'f':
            f();
            esp_letra();
            break;
        case 'g':
            g();
            esp_letra();
            break;
        case 'h':
            h();
            esp_letra();
            break;
        case 'i':
            i();
            esp_letra();
            break;
        case 'j':
            j();
            esp_letra();
            break;
        case 'k':
            k();
            esp_letra();
            break;
        case 'l':
            l();
            esp_letra();
            break;
        case 'm':
            m();
            esp_letra();
            break;
        case 'n':
            n();
            esp_letra();
            break;
        case 'o':
            o();
            esp_letra();
            break;
        case 'p':
            p();
            esp_letra();
            break;
        case 'q':
            q();
            esp_letra();
            break;
        case 'r':
            r();
            esp_letra();
            break;
        case 's':
            s();
            esp_letra();
            break;
        case 't':
            t();
            esp_letra();
            break;
        case 'u':
            u();
            esp_letra();
            break;
        case 'v':
            v();
            esp_letra();
            break;
        case 'w':
            w();
            esp_letra();
            break;
        case 'x':
            x();
            esp_letra();
            break;
        case 'y':
            y();
            esp_letra();
            break;
        case 'z':
            z();
            esp_letra();
            break;
        case '1':
            uno();
            esp_letra();
            break;
        case '2':
            dos();
            esp_letra();
            break;
        case '3':
            tres();
            esp_letra();
            break;
        case '4':
            cuatro();
            esp_letra();
            break;
        case '5':
            cinco();
            esp_letra();
            break;
        case '6':
            seis();
            esp_letra();
            break;
        case '7':
            siete();
            esp_letra();
            break;
        case '8':
            ocho();
            esp_letra();
            break;
        case '9':
            nueve();
            esp_letra();
            break;
        case '0':
            cero();
            esp_letra();
            break;
        case ' ':
            esp_palabra();
            break;
    }
}