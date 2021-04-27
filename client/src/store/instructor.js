import axios from 'axios'

export default {
    namespaced: true,
    actions: {
        async fetchInstructorReviews (_, request) {
            let response = await axios.get("/get-instructor-rev", {params: request}).catch(error => {
                console.log(error)
            })
            if (response.data.length != 0)
                return response.data
            else 
                return []
        },
        async postInstructorReviews (_, request) {
            let response = await axios.post("/get-instructor-rev", request).catch(error => {
                console.log(error)
            })
            return response.data
        }
    }
}