# fonctions annexes utiles
def produit_vectoriel(a, b):
    return a[0] * b[1] - a[1] * b[0]


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinéaire
    elif val > 0:
        return 1  # horaire
    else:
        return 2  # antihoraire


# algo naïf
def naive_algorithm(points):
    n = len(points)
    if n < 3:
        return points

    enveloppe = []

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            p1, p2 = points[i], points[j]
            left = 0
            right = 0

            for k in range(n):
                if k == i or k == j:
                    continue

                cp = produit_vectoriel(
                    (p2[0] - p1[0], p2[1] - p1[1]),
                    (points[k][0] - p1[0], points[k][1] - p1[1]),
                )

                if cp > 0:
                    left += 1
                elif cp < 0:
                    right += 1

            if left == 0 or right == 0:
                enveloppe.append(p1)
                enveloppe.append(p2)

    return list(set(enveloppe))


# divide and conquer
def cas_bases_enveloppe(points):
    n = len(points)
    if n <= 3:
        return points
    else:
        return naive_algorithm(points)


def divide_and_conquer(points):
    points = sorted(list(set(points)))
    n = len(points)
    if n <= 5:
        return cas_bases_enveloppe(points)

    milieu = n // 2
    enveloppe_gauche = divide_and_conquer(points[:milieu])
    enveloppe_droite = divide_and_conquer(points[milieu:])

    return fusionner(enveloppe_gauche, enveloppe_droite)


def fusionner(enveloppe_gauche, enveloppe_droite):
    enveloppe = []
    i_gauche = max(range(len(enveloppe_gauche)), key=lambda i: enveloppe_gauche[i][0])
    i_droite = min(range(len(enveloppe_droite)), key=lambda i: enveloppe_droite[i][0])
    n_gauche, n_droite = len(enveloppe_gauche), len(enveloppe_droite)

    t_g, t_d = i_gauche, i_droite
    done = False
    while not done:
        done = True
        while (
            orientation(
                enveloppe_droite[t_d],
                enveloppe_gauche[t_g],
                enveloppe_gauche[(t_g - 1) % n_gauche],
            )
            == 2
        ):
            t_g = (t_g - 1) % n_gauche
            done = False
        while (
            orientation(
                enveloppe_gauche[t_g],
                enveloppe_droite[t_d],
                enveloppe_droite[(t_d + 1) % n_droite],
            )
            == 1
        ):
            t_d = (t_d + 1) % n_droite
            done = False

    b_g, b_d = i_gauche, i_droite
    done = False
    while not done:
        done = True
        while (
            orientation(
                enveloppe_droite[b_d],
                enveloppe_gauche[b_g],
                enveloppe_gauche[(b_g + 1) % n_gauche],
            )
            == 1
        ):
            b_g = (b_g + 1) % n_gauche
            done = False
        while (
            orientation(
                enveloppe_gauche[b_g],
                enveloppe_droite[b_d],
                enveloppe_droite[(b_d - 1) % n_droite],
            )
            == 2
        ):
            b_d = (b_d - 1) % n_droite
            done = False

    enveloppe_fusionnee = []
    curr = t_g
    enveloppe_fusionnee.append(enveloppe_gauche[curr])
    while curr != b_g:
        curr = (curr + 1) % n_gauche
        enveloppe_fusionnee.append(enveloppe_gauche[curr])
    curr = b_d
    enveloppe_fusionnee.append(enveloppe_droite[curr])
    while curr != t_d:
        curr = (curr + 1) % n_droite
        enveloppe_fusionnee.append(enveloppe_droite[curr])

    return enveloppe_fusionnee


# jarvis
def jarvis(points):
    n = len(points)
    if n < 3:
        return points

    enveloppe = []
    point_gauche = min(points, key=lambda p: p[0])
    point_courant = point_gauche

    while True:
        enveloppe.append(point_courant)
        point_suivant = points[0]

        for p in points[1:]:
            if (
                point_suivant == point_courant
                or orientation(point_courant, point_suivant, p) == 2
            ):
                point_suivant = p

        point_courant = point_suivant

        if point_courant == point_gauche:
            break

    return enveloppe


# sklansky
def sklansky(polygone):
    n = len(polygone)
    if n < 3:
        return polygone

    enveloppe = []
    for i in range(n):
        while (
            len(enveloppe) >= 2
            and orientation(enveloppe[-2], enveloppe[-1], polygone[i]) != 2
        ):
            enveloppe.pop()
        enveloppe.append(polygone[i])

    return enveloppe
