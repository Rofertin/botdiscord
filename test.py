from datetime import date, datetime

fecha_hoy = date.today()
fecha_x = date(2021,2,25)
dfecha = fecha_hoy - fecha_x
print(fecha_x ,(dfecha), type(fecha_x), str(dfecha).split())