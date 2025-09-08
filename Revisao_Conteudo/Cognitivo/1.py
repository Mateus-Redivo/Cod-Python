def p(d, f=0.1, t=10):
    r = []
    for i in range(len(d)):
        if isinstance(d[i], dict):
            v = 0
            for k in d[i]:
                if k.startswith('val'):
                    v += d[i][k]
                elif k == 'mult' and i > 0:
                    v += d[i][k] * p(d[:i], f, t-1)[0] if t > 0 else 0
            if v > 0:
                tx = v * f if i % 3 == 0 else v * (f/2)
                v = v - tx if v > 100 else v - (tx/2)
                if 'special' in d[i] and d[i]['special']:
                    if d[i].get('type') == 'A':
                        v *= 1.5
                    elif d[i].get('type') == 'B':
                        v *= 1.2
                    else:
                        v *= 1.1
            r.append(v)
        else:
            r.append(d[i] * 0.8 if d[i] > 50 else d[i] * 0.9)
    return r


resultado = p([30, 60, 100])
print(resultado)
