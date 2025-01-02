#create some variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

#update scoring variables based on the activity choice
if activity == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1
    
    