from django.shortcuts import render
from django.http import HttpResponse

# from myapp.HybridCry import textfiletobinaryfile as tfb
# from myapp.HybridCry import breakintothreeparts as b3t
# from myapp.HybridCry import enc
# from myapp.HybridCry import mergeenc as mge

# from myapp.HybridCry import divideenc as de
# from myapp.HybridCry import desc
# from myapp.HybridCry import merge as m

from myapp.HybridCry import encryptcom as ec
from myapp.HybridCry import decryptioncom as de

# Create your views here.

def index(request):
    return render(request,"index.html")

def aboutus(request):
    print("Encryption process started: -")
    print()

    ec.encyptions()

    # tfb.TxtToBin()
    # b3t.BreakIn3Parts()
    # k=enc.keygen()
    # iv=enc.aesenc()
    # di=enc.desenc()
    # r=enc.rc4enc()
    # l=enc.decauth()
    # enc.stegnoimg(k,iv,di,r,l)

    # mge.MergeIn1()

    print("Encryption process completed")
    return render(request,"about.html",context={"m":"Encryption process completed"})

def contact(request):
    print("Decryption process started: -")
    print()

    de.decryptions()

    # l=de.stegnoimg()
    # de.DiviIn3(l)

    # # os.remove("f2\mergeenc.bin")

    # desc.stegnoimg()

    # # os.remove("s1.png")

    # desc.keygen()
    # desc.aesdec()
    # desc.desdec()
    # desc.rc4dec()

    # m.MergeIn3()
    print("Decryption process completed")
    return render(request,"contact.html",context={"m":"Decryption process completed"})

def service(request):
    return render(request,"service.html")

def msg(request):
    return render(request,"msg.html")