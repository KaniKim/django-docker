<template>
  <div>
    <table>
      <thread>
        <tr>
          <th>id</th>
          <th>제품명</th>
          <th>가격</th>
          <th>카테고리</th>
          <th>배송료</th>
        </tr>
      </thread>
      <tbody>
        <div v-if="isLoaded">
          <tr :key="i" v-for="{ product, i } in productList.data">
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.category }}</td>
            <td>{{ product.delivery_price }}</td>
          </tr>
        </div>
        <div v-else>Loading...</div>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      isLoaded: false,
      productList: [],
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData: function () {
      axios
        .get("/list/")
        .then(function (response) {
          self.productList = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}
td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
</style>