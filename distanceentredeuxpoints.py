# Écrire un programme qui demande à l’utilisateur les coordonnées de deux points dans le
# plan et qui calcule puis affiche la distance entre ces deux points selon la formule : d =
# \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}

# -*- coding:utf-8 -*-
import math
print “xA?”
xA = int(raw_input())
print “yA?”
yA = int(raw_input())
print "xB?"
xB = int(raw_input())
print "yB?"
yB = int(raw_input())
print "distance entre A et B:", math.sqrt( (xA-xB)**2 + (yA-yB)**2)
