# import divideenc as de
# import desc
# import merge as m
import os

from myapp.HybridCry import divideenc as de
from myapp.HybridCry import desc
from myapp.HybridCry import merge as m


def decryptions():
    print("Decryption process started: -")
    print()

    l=de.stegnoimg()
    de.DiviIn3(l)

    os.remove("myapp\HybridCry\F2\mergeenc.bin")

    desc.stegnoimg()

    os.remove("myapp\HybridCry\s1.png")

    desc.keygen()
    desc.aesdec()
    desc.desdec()
    desc.rc4dec()

    m.MergeIn3()

    print("Decryption process completed")