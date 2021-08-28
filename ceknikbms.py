import requests,os,sys
import datetime

def cekNik(url):
    response = requests.get(url, headers={"Accept":"application/json"})
    while response.status_code==200:
        try:
            os.system('clear')
            result=response.json()
            print("========================================")
            print("==            Data Ditemukan          ==")
            print("========================================")
            print("NIK : "+str(result['nik']))
            print("Nama : "+result['nama'])
            print("Tempat/Tanggal Lahir : "+result['tempat_lahir']+"/"+result['tgl_lahir'])
            print("Jenis Kelamin : "+result['jenis_kelamin'])
            print("Alamat : Rt."+str(result['rt'])+" Rw."+str(result['rw'])+" Desa "+result['kelurahan']+", Kecamatan "+result['kecamatan']+", Kabupaten "+result['kabupaten']+", Provinsi "+result['provinsi'])
            print("Agama : "+result['agama'])
            print("Pekerjaan : "+result['pekerjaan'])
            print("Golongan Darah :"+result['gol_darah'])
            break
        except ValueError:
            print("========================================")
            print("==     Maaf, Data Tidak Ditemukan     ==")
            print("========================================")
            break
# def main():
#     os.system("clear")
#     nik= input("NIK :   ")
#     url= "http://masbasid.banyumaskab.go.id/submit/ceknik?nik="+nik
#     print("")
#     cekNik(url)
if __name__=='__main__':
    os.system("clear")
    nik= input("NIK :   ")
    url= "http://masbasid.banyumaskab.go.id/submit/ceknik?nik="+nik
    print("")
    cekNik(url)