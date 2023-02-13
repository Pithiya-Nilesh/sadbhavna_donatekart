<template>
  <div>
    <router-view />
    <Toasts />
  </div>
</template>
<script>
import { provide, ref } from "vue"
import { call } from "frappe-ui"
import { Toasts } from "@/utils/toasts"
// import VueCardStack from "vue-card-stack";

export default {
	name: "App",
	components: {
		Toasts,
	},
  setup(){
    const user = ref({})
    provide("user", user)
    return { user }
  },
  mounted() {
      window.addEventListener("online", () => {
        this.$clearToasts()
        this.$toast({
          title: "You're online now",
          icon: "wifi",
          iconClasses: "stroke-green-600",
          appearance: "success",
          position: "bottom-right",
        })
      })
      window.addEventListener("offline", () => {
        this.$toast({
          title: "You're offline now",
          icon: "wifi-off",
          iconClasses: "stroke-red-600",
          appearance: "danger",
          fixed: true,
          position: "bottom-right",
        })
      })
      this.user = {
        isLoggedIn: () => {
          const cookie = Object.fromEntries(
            document.cookie
              .split("; ")
              .map((part) => part.split("="))
              .map((d) => [d[0], decodeURIComponent(d[1])])
            )
          return cookie.user_id && cookie.user_id !== "Guest"
        },
      }
    }
  }
</script>

