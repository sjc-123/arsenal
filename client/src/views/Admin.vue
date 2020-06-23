<template>
  <div>
    <b-tabs type="is-boxed">
      <b-tab-item label="球员信息">
        <b-table
          :data="playerInfo"
          :columns="playerInfoColumns"
        ></b-table>
      </b-tab-item>

      <b-tab-item label="球员比赛数据">
        <b-table
          :data="playerStat"
          :columns="playerStatColumns"
        ></b-table>
      </b-tab-item>

      <b-tab-item label="教练">
        <b-table
          :data="coach"
          :columns="coachColumns"
        ></b-table>
      </b-tab-item>
    </b-tabs>

    <b-field label="控制台">
      <b-input type="textarea" v-model="cmd"></b-input>
    </b-field>
    <b-button
      type="is-danger" size="is-medium" icon-left="send"
      @click="sendCmd()"
    >执行</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      playerInfo: [],
      playerInfoColumns: [
        {field: 'season', label: '赛季'},
        {field: 'player_id', label: '球衣号码'},
        {field: 'name', label: '姓名'},
        {field: 'position', label: '位置'},
        {field: 'birthdate', label: '生日'},
        {field: 'nationality', label: '国籍'},
        {field: 'height', label: '身高(cm)'},
        {field: 'weight', label: '体重(kg)'}
      ],
      playerStat: [],
      playerStatColumns: [
        {field: 'game_id', label: '比赛编号'},
        {field: 'league', label: '联赛'},
        {field: 'season', label: '赛季'},
        {field: 'player_id', label: '球员球衣号码'},
        {field: 'opponent', label: '对手'},
        {field: 'score', label: '进球数'},
        {field: 'yellow_card', label: '黄牌数'},
        {field: 'red_card', label: '红牌数'}
      ],
      coach: [],
      coachColumns: [
        {field: 'season', label: '赛季'},
        {field: 'name', label: '教练'}
      ],
      cmd: ''
    }
  },

  methods: {
    sendCmd() {
      fetch(process.env.VUE_APP_APIURL + '/execsql', {
        method: 'POST',
        headers: {'content-type': 'application/json'},
        body: JSON.stringify({'cmd': this.cmd})
      })
      .then(res => res.json())
      .then(res => alert(res))
    }
  },

  beforeMount(){
    fetch(process.env.VUE_APP_APIURL + '/info')
    .then(res => res.json())
    .then(r => {this.playerInfo = r})

    fetch(process.env.VUE_APP_APIURL + '/stat')
    .then(res => res.json())
    .then(r => {this.playerStat = r})

    fetch(process.env.VUE_APP_APIURL + '/coach')
    .then(res => res.json())
    .then(r => {this.coach = r})
  }
}
</script>
