datauser = {
            "tommy123" : {
                        "Password" : "Tommy123$",
                        "Email" : "tommysachi@hotmail.com",
                        "Nama" : "Tommy",
                        "Gender" : "Male",
                        "Usia" : 25,
                        "Pekerjaan" : "",
                        "Hobi" : "",
                        "No HP" : "",
                        "Alamat" : {
                                "Nama Kota" : "",
                                "RT" : "",
                                "RW" : "",
                                "Zip Code" : "",
                                "Geo" : {
                                    "Latitude" : "",
                                    "Longitude" : ""
                                }
                        }   
            }
                
    }   

databarang = {
            "Iphone" : 15000000,
            "Samsung" : 12000000,
            "Huawei" : 10000000,
            "LG" : 8000000,
            "Xiaomi :" :6000000,
            "Oppo" : 4000000,
            "Vivo" : 2000000
}

def menuawal():
    print("SELAMAT DATANG DI APLIKASI STOCK HP")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan1 = int(input("Pilih Command : "))
    if pilihan1 == 1:
        registerglobal()
        menuawal()
    elif pilihan1 == 2:
        for i in range(1,6):
            userid = str(input("Masukkan User ID : "))
            password = str(input("Masukkan Password : ")) 
            perintah = login(i,userid,password,datauser)
            if perintah != True:
                print(perintah)
            elif perintah == True:
                print("1. User Profile")
                print("2. Menu Transaksi")
                pilihan2 = int(input("Pilih Command : "))
                if pilihan2 == 1:
                    print("Data Anda : ")
                    nama = datauser[userid]["Nama"]
                    email = datauser[userid]["Email"]
                    gender = datauser[userid]["Gender"]
                    usia = datauser[userid]["Usia"]
                    pekerjaan = datauser[userid]["Pekerjaan"]
                    hobi = datauser[userid]["Hobi"]
                    kota = datauser[userid]["Alamat"]["Nama Kota"]
                    rt = datauser[userid]["Alamat"]["RT"]
                    rw = datauser[userid]["Alamat"]["RW"]
                    zipcode = datauser[userid]["Alamat"]["Zip Code"]
                    lat = datauser[userid]["Alamat"]["Geo"]["Latitude"]
                    lon = datauser[userid]["Alamat"]["Geo"]["Longitude"]
                    hp = datauser[userid]["No HP"]
                    print(f"Email    : {nama}")
                    print(f"Email    : {email}")
                    print(f"Gender   : {gender}")
                    print(f"Usia     : {usia}")
                    print(f"Pekerjaan: {pekerjaan}")
                    print(f"Hobi     : {hobi}")
                    print(f"Alamat   : ")
                    print(f"  Nama Kota  : {kota}")
                    print(f"  RT         : {rt}")
                    print(f"  RW         : {rw}")
                    print(f"  Zip Code   : {zipcode}")
                    print(f"  Geo        : ")
                    print(f"    Lat        : {lat}")
                    print(f"    Long       : {lon}")
                    print(f"No HP    : {hp}")
                    break
                elif pilihan2 == 2:
                    menucrud(databarang)
                    break
          
    elif pilihan1 == 3:
        exit()

def register1(userid):
    specialchar = ["&","^","%","$","#","!","@"]
    datakeys = list(datauser.keys())
    banyakdatakeys = len(datakeys)
    if userid.isdigit() or userid.isalpha():
        return "User ID Harus Huruf dan Angka"
    elif len(userid) < 6 or len(userid) > 20:
        return "User ID Minimal 6 Karakter dan Maksimal 10 Karakter"
    elif userid in datakeys[0:banyakdatakeys+1]:
        return "User ID Sudah Terdaftar"
    else:
        for j in specialchar:
            cek = False
            if j in userid:
                cek = True
                break
            else:
                cek = False
        if cek == True :
            return "Tidak Boleh ada Special Character"
        else:
            return True

def register2(password):
    specialchar = ["&","^","%","$","#","!","@"]

    if len(password) < 8:
        return "Password Harus Minimal 8 Karakter"
    elif password.isupper() or password.islower():
        return "Harus Kombinasi Huruf Kapital dan Kecil"
    else:
        for j in specialchar:
            cek = False
            if j in password:
                cek = True
                break
            else:
                cek = False
        if cek == True :
            return True
        else:
            return "Harus Ada Special Character"

def register3(email):
    panjang = len(email)
    cek1 = "@"
    cek2 = "."
    cek3 = '''`!#$%^&*()+=-[{]};:<,>/?'"'''
    cek4 = '''`!#$%^&*()_+=-[{]};:<,>/?'".'''
    cek5 = '''`!#$%^&*()_+=-[{]};:<,>/?'"0123456789'''
    at = 0
    titik = 0
    for i in email :
        for j in cek1 :
            if i == j :
                at += 1
    if at > 1:
        return "Email INVALID Format Email Salah"
    elif at < 1:
        return "Email INVALID Format Email Salah"
    elif at == 1:
        x = email.index("@")
        email1 = email[x+1:panjang]
        email2 = email[0:x]
        for i in email1:
            for j in cek2 :
                if i == j :
                    titik += 1  
        if titik > 2 or titik < 1:
            return "Email INVALID Format Email Salah"
        elif not(email[0].isalnum()):
            return "Email INVALID Format Email Salah"
        elif titik >= 1 or titik <=2:
            for i in email2:
                for j in cek3:
                    if i == j :
                        return "Email INVALID Format Username Salah" 
                        break
                if i == j :
                    break
            else :     
                y = email1.index(".")
                email3 = email1[0:y]
                email4 = email1[y+1:panjang]

                for k in email3:
                    for l in cek4:
                        if k == l :
                            return "Email INVALID Format Hosting Salah"
                            break
                    if k == l :
                        break
                else :
                    for m in email4:
                        for n in cek5:
                            if m == n or len(email4)>5 :
                                return "Email INVALID Format Extension Salah"
                                break
                        if m == n or len(email4)>5:
                            break
                    else:
                        return True

def register4(nama,gender,usia,pekerjaan,hobi,kota,RT,RW,zipcode,hp,ceklat,ceklon):
    jumlahhobi = hobi.split(" ")
    if not(nama.isalpha()):
        return "Nama Hanya Alfabet"
    elif gender != "Male" and gender != "Female":
        return "Isi Male atau Female"
    elif usia<=17 or usia>=80:
        return "Usia minimal 17 dan maksimal 80"
    elif pekerjaan.isdigit():
        return "Pekerjaan Hanya Alfabet"
    elif hobi.isdigit() or len(jumlahhobi)<=1:
        return "Isi Hobi Lebih dari 1 dan Hanya Alfabet"
    elif kota.isdigit():
        return "Nama Kota Hanya Alfabet"
    elif RT.isalpha():
        return "RT Harus Numerik Integer"
    elif RW.isalpha():
        return "RW Harus Numerik Integer"
    elif zipcode.isalpha() or len(zipcode) < 5:
        return "Kode Pos Harus Numerik Integer atau Minimal 5 Angka"
    elif ceklat == False :
        return "Latitude Numerik - Float Integer"
    elif ceklon == False :
        return "Longitude Numerik - Float Integer"
    elif hp.isalpha() or len(hp)<=11 or len(hp)>=13:
        return "No HP Numerik - Kurang dari 11 digit atau Lebih dari 13 digit"
    else:
        return True

def registerglobal():
    for i in range(1,7):
        userid = str(input("UserID : "))
        note1 = register1(userid)
        if i < 5 and note1 != True:
            print(note1)
        elif i ==5 and note1 != True:
            print(note1)
            print("Sudah 5 Kali Percobaan")
            exit()
        else:
            break

    for j in range(1,7):
        password = str(input("Password : "))
        note2 = register2(password)
        if j < 5 and note2 != True:
            print(note2)
        elif j ==5 and note2 != True:
            print(note2)
            print("Sudah 5 Kali Percobaan")
            exit()
        else:
            break

    for k in range(1,7):
        email = str(input("Email : "))
        note3 = register3(email)
        if k < 5 and note3 != True:
            print(note3)
        elif k ==5 and note3 != True:
            print(note3)
            print("Sudah 5 Kali Percobaan")
            exit()
        else:
            break
    note4 = False
    while note4 != True:
        nama = str(input("Nama : "))
        gender = str(input("Gender : "))
        usia = int(input("Usia : "))
        pekerjaan = str(input("Pekerjaan : "))
        hobi = str(input("Hobi : "))
        kota = str(input("Nama Kota : "))
        RT = str(input("RT : "))
        RW = str(input("RW : "))
        zipcode = str(input("Zip Code : "))
        try :
            lat = float(input("Latitude : "))
            ceklat = True
        except :
            ceklat = False
        try :
            lon = float(input("Longitude : "))
            ceklon = True
        except :
            ceklon = False
        hp = str(input("No HP : "))
        note4 = register4(nama,gender,usia,pekerjaan,hobi,kota,RT,RW,zipcode,hp,ceklat,ceklon)
        if note4 != True:
            print(note4)
    
    simpan = input("Simpan Data (Y/N) : ")
    if simpan == "N" :
        menuawal()
    elif simpan == "Y" :
        datauser[userid] = {}
        datauser[userid]["Password"] = password
        datauser[userid]["Email"] = email
        datauser[userid]["Nama"] = nama
        datauser[userid]["Gender"] = gender
        datauser[userid]["Usia"] = usia
        datauser[userid]["Pekerjaan"] = pekerjaan
        datauser[userid]["Hobi"] = hobi
        datauser[userid]["Alamat"] = {}
        datauser[userid]["Alamat"]["Nama Kota"] = kota
        datauser[userid]["Alamat"]["RT"] = RT
        datauser[userid]["Alamat"]["RW"] = RW
        datauser[userid]["Alamat"]["Zip Code"] = zipcode
        datauser[userid]["Alamat"]["Geo"] = {}
        datauser[userid]["Alamat"]["Geo"]["Latitude"] = lat
        datauser[userid]["Alamat"]["Geo"]["Longitude"] = lon
        datauser[userid]["No HP"] = hp
    else:
        print("Salah Keyword, Akan Exit ke Menu Awal")
        menuawal() 
            
def login(i,userid,password,datauser):
    user = list(datauser.keys())
    pas = str(datauser[userid]["Password"])   
    if i <= 5 and userid in user and password == pas:
        return True
    elif i <= 5 and userid in user and password != pas:
        return "Password Salah"
    else:
        return "User ID Tidak Terdaftar"

def menucrud(databarang):
    print("1. Read Data")
    print("2. Create Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Kembali ke Menu Awal")
    pilihan = int(input("Pilih Command : "))
    if pilihan == 5:
        menuawal()
    elif pilihan == 4:
        databarang.pop(deletedata())
        print(list(databarang.items()))
        return menucrud(databarang)
    elif pilihan == 1:
        print(readdata(databarang))
        return menucrud(databarang)
    elif pilihan == 2:
        print(createdata(databarang))
        return menucrud(databarang)
    else:
        print(updatedata(databarang))
        return menucrud(databarang)

def readdata(databarang):
    data = list(databarang.items())
    if len(data) == 0:
        return "Tidak ada Data"
    else:
        return list(databarang.items())

def deletedata():
    hapus = str(input("Delete : "))
    return hapus

def createdata(databarang):
    barang = str(input("Nama Barang : "))
    harga = str(input("Harga Barang : "))
    data = list(databarang.keys())
    if barang.isdigit() or harga.isalpha():
        return "Format Salah"
    else:
        for i in data:
            if i == barang:
                print("Barang Sudah Terinput")
                perintah = input("Apakah Ingin Update Data ? (Y/N)")
                if perintah == "Y":
                    databarang[barang]=harga
                    return list(databarang.items())
                elif perintah == "N":
                    return "Data Tidak Tersimpan"
            else:
                databarang[barang]=harga
                return list(databarang.items())

def updatedata(databarang):
    barang = str(input("Nama Barang : "))
    harga = int(input("Harga Barang : "))
    data = list(databarang.keys())
    if barang in data:
        databarang[barang]=harga
        return list(databarang.items())
    else:
        return "Data barang tidak ditemukan"

menuawal()