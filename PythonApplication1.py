from PIL import Image
import numpy as np

#mengubah gambar ke array
img = Image.open ("foto.png")
numpy_array = np.array(img)


#ini untuk test mencoba bentuknya array kayak apa
warna = numpy_array[0,0]
print("print bentuk lengkap array nya", warna)

#logika untuk hanya menampilkan 3 warna pertama
kodewarna = warna[:3]
print("seharusnya ngeprint 3 warna utama rgb nya", kodewarna)

total = sum(kodewarna.astype(int))
print("totalnya warna", total)
print("kalo di bagi mod hasilnya segini", total %2)

#logika untuk steganografi

kode = "0110100001100101011011000110110001101111" #ini hello kalo di biner 
index_pesan = 0
tinggi, lebar, _ = numpy_array.shape
for y in range(tinggi):
    for x in range(lebar):
        if index_pesan < len(kode):
            target = int(kode[index_pesan])
            rgb =numpy_array[y, x, :3].astype(int)
            total = sum(rgb)
            sisa_bagi = total %2
            if sisa_bagi != target:
                if numpy_array[y, x, 0] ==255:
                    numpy_array[y, x, 0] -=1
                if numpy_array[y, x, 0] ==0:
                    numpy_array[y, x, 0] +=1
                else:
                    numpy_array[y, x, 0] +=1
            index_pesan += 1
        else:
            break
    if index_pesan >= len(kode):
      break

img_baru = Image.fromarray(numpy_array)
img_baru.save("gamar_terbaru.png")
print("harusnya udah jadi")