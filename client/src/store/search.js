import axios from 'axios'

export default {
    namespaced: true,
    actions: {
        async courseSearch (_, request) {
            let response = await axios.get("/get-courses", {params: request}).catch(error => {
                console.log(error)
            })
            return response.data
        },
        async instructorSearch (_, request) {
            let response = await axios.get("/get-instructor", {params: request}).catch(error => {
                console.log(error)
            })
            return response.data
        }
    }
}