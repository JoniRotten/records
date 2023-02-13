import cx_Oracle
import tkinter as tk
import config

def insert_data():
    # obtener los datos del formulario
    a_name = entry_a_name.get()
    name = entry_name.get()
    year = entry_year.get()
    formato = entry_format.get()
    comentario = entry_comentario.get()
    shop = entry_shop.get()
    prize = entry_prize.get()
    day = entry_day.get()
    nuevo = entry_nuevo.get()
    photo = entry_photo.get()
    numero = entry_numero.get()
    cd = entry_cd.get()
    digital = entry_digital.get()
    single = entry_single.get()
    dvd = entry_dvd.get()
    place = entry_place.get()
    discogs = entry_discogs.get()

    # conectarse a la base de datos Oracle
    con = cx_Oracle.connect(
             config.username,
             config.password,
             config.dsn,
             encoding=config.encoding)
    cursor = con.cursor()

    # insertar los datos en la tabla
    sql = "insert into records (a_name, name, year, formato, com, shop, prize, day, place, new, photo, t_number, cd, digital, single, dvd, control, sitio, discogs) values (:a_name, :name, to_date(:year,'yyyy'), :formato, :comentario, :shop, :prize, to_date(:day,'yyyy-mm-dd')\
    , :place, :nuevo, :photo, :numero, :cd, :digital, :single, :dvd, '1', 'Corsega', substr(substr(:discogs,3),0,length(substr(:discogs,3))-1))"
    cursor.execute(sql, {'a_name': a_name, 'name': name, 'year': year, 'formato': formato, 'comentario': comentario, 'shop': shop, 'prize': prize, 'day': day, 'place': place, 'nuevo': nuevo, 'photo': photo, 'numero': numero, 'cd': cd, 'digital': digital, 'single': single, 'dvd': dvd, 'discogs': discogs})
    con.commit()

    # cerrar la conexión a la base de datos
    cursor.close()
    con.close()

    # mostrar un mensaje de éxito
    label_result.config(text="Datos ingresados correctamente")

# crear la ventana principal
root = tk.Tk()
root.title("Formulario de ingreso de datos")

# crear los widgets
label_a_name = tk.Label(root, text="Artist")
entry_a_name = tk.Entry(root)
label_name = tk.Label(root, text="Title")
entry_name = tk.Entry(root)
label_year = tk.Label(root, text="Year")
entry_year = tk.Entry(root)
label_format = tk.Label(root, text="Format")
entry_format = tk.Entry(root)
label_comentario = tk.Label(root, text="Comment")
entry_comentario = tk.Entry(root)
label_shop= tk.Label(root, text="shop")
entry_shop = tk.Entry(root)
label_prize = tk.Label(root, text="Prize")
entry_prize = tk.Entry(root)
label_day = tk.Label(root, text="Day Bought yyyy-mm-dd")
entry_day = tk.Entry(root)
label_nuevo = tk.Label(root, text="New (1=YES 0=NO)")
entry_nuevo = tk.Entry(root)
label_photo = tk.Label(root, text="Photo (1=YES 0=NO)")
entry_photo = tk.Entry(root)
label_numero = tk.Label(root, text="Number")
entry_numero = tk.Entry(root)
label_cd = tk.Label(root, text="Extra CD")
entry_cd = tk.Entry(root)
label_digital = tk.Label(root, text="Digital download (1=YES 0=NO)")
entry_digital = tk.Entry(root)
label_single = tk.Label(root, text="Extra single")
entry_single = tk.Entry(root)
label_dvd = tk.Label(root, text="Extra dvd")
entry_dvd = tk.Entry(root)
label_place = tk.Label(root, text="Place")
entry_place = tk.Entry(root)
label_discogs = tk.Label(root, text="Discogs")
entry_discogs = tk.Entry(root)
button_submit = tk.Button(root, text="Ingresar datos", command=insert_data)
label_result = tk.Label(root)

# posicionar los widgets en la ventana
label_a_name.grid(row=0, column=0)
entry_a_name.grid(row=0, column=1)
label_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)
label_year.grid(row=2, column=0)
entry_year.grid(row=2, column=1)
label_format.grid(row=3, column=0)
entry_format.grid(row=3, column=1)
label_comentario.grid(row=4, column=0)
entry_comentario.grid(row=4, column=1)
label_shop.grid(row=5, column=0)
entry_shop.grid(row=5, column=1)
label_prize.grid(row=6, column=0)
entry_prize.grid(row=6, column=1)
label_day.grid(row=7, column=0)
entry_day.grid(row=7, column=1)
label_nuevo.grid(row=8, column=0)
entry_nuevo.grid(row=8, column=1)
label_photo.grid(row=9, column=0)
entry_photo.grid(row=9, column=1)
label_numero.grid(row=10, column=0)
entry_numero.grid(row=10, column=1)
label_cd.grid(row=11, column=0)
entry_cd.grid(row=11, column=1)
label_digital.grid(row=12, column=0)
entry_digital.grid(row=12, column=1)
label_single.grid(row=13, column=0)
entry_single.grid(row=13, column=1)
label_dvd.grid(row=14, column=0)
entry_dvd.grid(row=14, column=1)
label_place.grid(row=15, column=0)
entry_place.grid(row=15, column=1)
label_discogs.grid(row=16, column=0)
entry_discogs.grid(row=16, column=1)
button_submit.grid(row=18, column=0, columnspan=2, pady=10)
label_result.grid(row=19, column=0, columnspan=2)

# ejecutar la ventana
root.mainloop()
