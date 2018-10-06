# this program provides a transliteration of english to bengali of a phrase in the following form:
# "pronoun action pronoun"
# for eg. "she needed him"

sub=str(input()) # input pronoun of subject
verb=str(input()) # input verb
obj=str(input()) # input pronoun of object

# all input must be in lower case letters

sub_first=["i", "we"]
t_sub_first=["ami", "amra"]

sub_second=["you"]
t_sub_second=["tumi"]

sub_third=["he", "she", "they"]
t_sub_third=["shey", "shey", "ora"]

obj_first=["me", "us"]
t_obj_first=["amake", "amader ke"]

obj_second=["you"]
t_obj_second=["tomake"]

obj_third=["him", "her", "them"]
t_obj_third=["oke", "oke", "oder ke"]

v_present=["make", "know", "take", "see", "want", "give", "tell", "call", "ask", "need", "keep", "help", "show", "hear", "believe", "write", "lose", "meet", "understand", "stop", "kill", "love", "hate", "like", "eat", "break"]
t_v_present_first=["banai", "chini", "niye jai", "dekhi", "chai" "dei", "boli", "daki", "jiggesh kori", "chai", "rakhi", "dei", "shahajjo kori", "dekhai", "shuni", "bishshaash kori", "likhi", "harai", "dekhi", "bujhi", "thamai", "khun kori", "bhalobashi", "ghreena kori", "pochondo kori", "khai", "bhenge dei"]
t_v_present_second=["banao", "chino", "niye jao", "dekho", "chao" "dao", "bolo", "dako", "jiggesh koro", "chao", "rakho", "dao", "shahajjo koro", "dekhao", "shuno", "bishshaash koro", "likho", "harao", "dekho", "bujho", "thamao", "khun koro", "bhalobasho", "ghreena koro", "pochondo koro", "khao", "bhenge dao"]
t_v_present_third=["banai", "chine", "niye jai", "dekhe", "chai" "dei", "bole", "dake", "jiggesh kore", "chai", "rakhe", "dei", "shahajjo kore", "dekhai", "shune", "bishshaash kore", "likhe", "harai", "dekhe", "bujhe", "thamai", "khun kore", "bhalobashe", "ghreena kore", "pochondo kore", "khai", "bhenge dei"]

v_past=["made", "knew", "took", "saw", "wanted", "gave", "told", "called", "asked", "needed", "kept", "helped", "showed", "heard", "believed", "wrote", "lost", "met", "understood", "stopped", "killed", "loved", "hated", "liked", "ate", "broke"]
t_v_past_first=["baniyechi", "chintam", "niyechi", "dekhechi", "chaitam", "diyechi", "bolechi", "dekechi", "jiggesh korechi", "chaitam", "rekhechi", "shahajjo korechi", "dekhiyechi", "shunechi", "bishshaash korechi", "likhechi", "hariyechi", "dekhechi", "bujhechi", "thamiyechi", "khun korechi", "bhalobashtam", "ghreena kortam", "pochondo kortam", "kheyechi", "bhenge diyechi"]
t_v_past_second=["baniyechila", "chinta", "niyechila", "dekhechila", "chaita", "diyechila", "bolechila", "dekechila", "jiggesh korechila", "chaita", "rekhechila", "shahajjo korechila", "dekhiyechila", "shunechila", "bishshaash korechila", "likhechila", "hariyechila", "dekhechila", "bujhechila", "thamiyechila", "khun korechila", "bhalobashta", "ghreena korta", "pochondo korta", "kheyechila", "bhenge diyechila"]
t_v_past_third=["baniyeche", "chinto", "niyeche", "dekheche", "chaito", "diyeche", "boleche", "dekeche", "jiggesh koreche", "chaito", "rekheche", "shahajjo koreche", "dekhiyeche", "shuneche", "bishshaash koreche", "likheche", "hariyeche", "dekheche", "bujheche", "thamiyeche", "khun koreche", "bhalobashto", "ghreena korto", "pochondo korto", "kheyeche", "bhenge diyeche"]

tsub=0
tverb=0
tobj=0
x=0

if sub in sub_first:
    x=1
    tsub=t_sub_first[sub_first.index(sub)]
elif sub in sub_second:
    x=2
    tsub=t_sub_second[sub_second.index(sub)]
elif sub in sub_third:
    x=3
    tsub=t_sub_third[sub_third.index(sub)]

if x==1:
    if verb in v_present:
        tverb=t_v_present_first[v_present.index(verb)]
    elif verb in v_past:
        tverb=t_v_past_first[v_past.index(verb)]
elif x==2:
    if verb in v_present:
        tverb=t_v_present_second[v_present.index(verb)]
    elif verb in v_past:
        tverb=t_v_past_second[v_past.index(verb)]
elif x==3:
    if verb in v_present:
        tverb=t_v_present_third[v_present.index(verb)]
    elif verb in v_past:
        tverb=t_v_past_third[v_past.index(verb)]

if obj in obj_first:
    tobj=t_obj_first[obj_first.index(obj)]
elif obj in obj_second:
    tobj=t_obj_second[obj_second.index(obj)]
elif obj in obj_third:
    tobj=t_obj_third[obj_third.index(obj)]

if tsub==0 or tverb==0 or tobj==0:
    print("sorry! we couldn't translate that for you")
else:
    print(str(tsub)+" "+str(tobj)+" "+str(tverb))
