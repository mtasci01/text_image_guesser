from fastapi import FastAPI, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from ITService import ITService

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = ITService()



@app.get("/text/get_saved_files")
def getSavedFiles():
    return service.getSavedTextFiles()

@app.get("/text/start_game")
def start_txt_game(docId,prob):
    return service.startTxtGame(docId,prob)

@app.get("/text/guess_word")
def guess_text_word(game_id,word):
    return service.guessTextWord(game_id,word)

@app.get("/text/reveal_number")
def text_reveal_number(game_id,number):
    return service.textRevealNumber(game_id,number)

@app.delete("/text/delete_file")
def delete_file(file_id):
    return service.delete_file(file_id)

@app.post("/text/upload_file")
def upload_file(file: UploadFile):
    return service.upload_file(file)

@app.get("/text/start_char_game")
def start_char_game(file_id,prob):
    return service.start_char_game(file_id,prob)

@app.post("/img/upload_labeled_file")
def upload_labeled_file(file: UploadFile, label):
    return service.upload_labeled_file(file,label)

@app.get("/img/get")
def get_labeled_img(doc_id):
    ret =   service.get_saved_img(doc_id)
    return Response(content=ret['img'], media_type="image/" +ret['ext'].replace('.',''))

@app.get("/img/get_saved_img_num")
def get_saved_img_num():
    return service.getNumOfImages()

@app.get("/img/start_game")
def start_img_game():
    ret=  service.start_img_game()
    return ret

@app.get("/img/download_cached")
def download_cached_img(game_id):
    ret =  service.download_cached_img(game_id)
    return Response(content=ret['img_bytes'], media_type="image/png")

@app.get("/img/click_img_sent")
def click_img_sent(p_x,p_y,client_img_size,game_id):
    ret=  service.click_img_sent([float(p_x),float(p_y)],float(client_img_size),game_id)
    return ret

@app.get("/img/get_all_labels")
def get_all_labels(): 
    return service.get_all_labels()

@app.get("/img/download_cached_original")
def download_cached_original(game_id):
    ret =  service.download_cached_original(game_id)
    return Response(content=ret['img_origin_bytes'], media_type="image/png")

@app.get("/img/clear_fs_cache")
def img_clear_fs_cache(): 
    return service.img_clear_fs_cache()

@app.post("/text/docx_char_scrambler")
def docx_scrambler(file: UploadFile, p_change):
    return Response(content=service.docx_char_scrambler(file,p_change), media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

@app.post("/text/docx_word_scrambler")
def docx_scrambler(file: UploadFile, p_change):
    return Response(content=service.docx_word_scrambler(file,p_change), media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

@app.get("/locations/get_all")
def get_all_locations(): 
    return service.get_all_locations()

@app.get("/locations/get_all_labels")
def get_all_location_labels(): 
    return service.get_all_location_labels()

@app.get("/locations/get_random_label")
def get_random_location_label(): 
    return service.get_random_location_label()

@app.get("/locations/get_directions")
def get_all_locations(start,target): 
    return service.get_directions(start,target)
