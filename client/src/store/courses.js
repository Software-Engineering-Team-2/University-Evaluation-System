import axios from 'axios'

export default {
    namespaced: true,
    actions: {
        async fetchCourseReviews (_, request) {
            let response = await axios.get("/get-course-rev", {params: request}).catch(error => {
                console.log(error)
            })
            return response.data
        },
        async postCourseReviews (_, request) {
            let response = await axios.post("/get-course-rev", request).catch(error => {
                console.log(error)
            })
            return response.data
        },
        async updateVotes(_, request) {
            let response = await axios.patch('get-course-rev', request).catch(error => {
                console.log(error)
            })
            return response.data
        },

        async getCourseReviewVotes(_, request) {
            let response = await axios.post('get-course-rev-votes', request).catch(error => {
                console.log(error)
            })
            return response.data
        }
    }
}