import flet as ft 
import serial 
import threading 
import time 
 
PUERTO = "COM5"   
BAUDIOS = 9600 
 
def main(page: ft.Page): 
    page.title = "Control de LED ESP32 (PWM)" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
 
     
    try: 
        arduino = serial.Serial(PUERTO, BAUDIOS, timeout=1) 
        time.sleep(2)  
    except Exception as e: 
        page.add(ft.Text(f"Error al conectar con {PUERTO}: {e}", color="red")) 
        return 
 
    pwm_text = ft.Text("Valor PWM actual: 0", size=20) 
 
    def enviar_valor(valor): 
        try: 
            comando = f"{valor}\n" 
            arduino.write(comando.encode()) 
            pwm_text.value = f"Valor PWM actual: {valor}" 
            page.update() 
        except Exception as e: 
            pwm_text.value = f" Error enviando datos: {e}" 
            page.update() 
 
    # Slider para controlar brillo 
    slider = ft.Slider( 
        min=0, 
        max=255, 
        divisions=255, 
 

        label="{value}", 
        value=0, 
        width=400, 
        on_change=lambda e: enviar_valor(int(e.control.value)), 
    ) 
 
    # Mostrar la interfaz 
    page.add( 
        ft.Text(" Control de LED con ESP32", size=25, 
weight=ft.FontWeight.BOLD), 
        slider, 
        pwm_text, 
    ) 
 
     
    def cerrar_conexion(e): 
        if arduino.is_open: 
            arduino.close() 
 
    page.on_close = cerrar_conexion 
 
ft.app(target=main) 

