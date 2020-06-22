from fastapi import FastAPI

app = FastAPI()

@app.get('/info')
def get_info():
    return [{
        'season': '10-11',
        'id': 1,
        'name': '金世豪',
        'position': '守门员',
        'birthdate': '77年05月',
        'nationality': '朝鲜',
        'height': 160,
        'weight': 70
    }]

@app.get('/stat')
def get_stat():
    return 'todo'

@app.get('/coach')
def get_coach():
    return 'todo'
