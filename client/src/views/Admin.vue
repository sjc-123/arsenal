<template>
  <div>
    <b-table :data="playerInfo" :columns="playerInfoColumns"></b-table>
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
      ]
    }
  },

  beforeMount(){
    fetch(process.env.VUE_APP_APIURL + '/info')
    .then(res => res.json())
    .then(r => {this.playerInfo = r})
  }
}
</script>
