from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/info')
def get_info():
    return [
        {
            'season': '10-11',
            'player_id': 1,
            'name': '金世豪',
            'position': '守门员',
            'birthdate': '77年05月',
            'nationality': '朝鲜',
            'height': 160,
            'weight': 70
        },
        {
            'season': '10-11',
            'player_id': 114514,
            'name': '田所浩二',
            'position': '守门员',
            'birthdate': '19年08月',
            'nationality': '下北泽',
            'height': 170,
            'weight': 80
        }
    ]


@app.get('/stat')
def get_stat():
    return [
        {
            'game_id': 0,
            'league': '英超',
            'season': '10-11',
            'player_id': 114514,
            'opponent': '切尔西',
            'score': 19,
            'yellow_card': 1,
            'red_card': 0
        }
    ]


@app.get('/coach')
def get_coach():
    return [
        {
            'season': '10-11',
            'name': '孙笑川'
        }
    ]
