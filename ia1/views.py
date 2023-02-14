from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
# from feedback.models import Feedback

def index(request):
    return render(request, 'index.html')


def Encrypt(request):
        if request.method=='POST':
            message=request.POST.get('ptext')
            p = 151
            q = 43
            public_key = p * q


            def encrypter(m, n):
                c = (m * m) % public_key
                return c


            def mod(k, b, m):
                i = 0
                a = 1
                t = []
                while k > 0:
                    t.append(k % 2)
                    k = (k - t[i]) // 2
                    i += 1
                for j in range(i):
                    if t[j] == 1:
                        a = (a * b) % m
                        b = (b * b) % m
                    else:
                        b = (b * b) % m
                return a


            def modulo(a, b):
                if a >= 0:
                    return (a % b)
                return ((b - abs(a % b)) % b)


            def Extended_Euclid(a, b):
                if b > a:
                    temp = a
                    a = b
                    b = temp
                x = 0
                y = 1
                lastx = 1
                lasty = 0
                while b != 0:
                    q = a // b
                    temp1 = a % b
                    a = b
                    b = temp1
                    temp2 = x
                    x = lastx - q * x
                    lastx = temp2
                    temp3 = y
                    y = lasty - q * y
                    lasty = temp3
                arr = [lastx, lasty, 1]
                return arr


            def decrypter(c, p, q):
                mp = mod((p + 1) // 4, c, p)
                mq = mod((q + 1) // 4, c, q)

                arr = Extended_Euclid(p, q)
                rootp = arr[0] * p * mq
                rootq = arr[1] * q * mp
                r = modulo((rootp + rootq), public_key)
                if r < 128:
                    return r
                negative_r = public_key - r
                if negative_r < 128:
                    return negative_r
                s = modulo((rootp - rootq), public_key)
                if s < 128:
                    return s
                negative_s = public_key - s
                return negative_s


            encrypted = []
            decrypted = []
            # message = input("Enter Text To Be Encrypted: ")
            print("Plain Text:", message)
            leng = len(message)
            print("Encrypted Text:", end="")
            for i in range(leng):
                encrypted.append(encrypter(ord(message[i]), public_key))
                print(encrypted[i], end="")
            print("")
            for i in range(leng):
                decrypted.append(decrypter(encrypted[i], p, q))
            print("Decrypted Text:", end="")
            output2=[]
            for i in decrypted:
                output2+=chr(i)
                print(chr(i), end="")
            print("")
            output=''
            for i in range(leng):
                output=''.join(map(str,encrypted))

     
            output2 = ''.join(output2)
            print(output2)

            return render(request, 'index.html', {'output1': output, 'output2': output2})



# def feedback(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         feedback = request.POST.get('feedback')
#         fb = Feedback(name=name, email=email, feedback=feedback)
#         fb.save()
#         return HttpResponseRedirect('/')

