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
            let response = await axios.post("/get-instructor-rev", request['review']).then(async (r) => {
                return await axios.patch('get-instructor-rev-tags', {tags: request['tags'], reviewId: r.data['id']})
            })
            return response.data
        },
        async updateVotes(_, request) {
            let response = await axios.patch('get-instructor-rev', request).catch(error => {
                console.log(error)
            })
            return response.data
        },

        async getInstructorReviewVotes(_, request) {
            let response = await axios.post('get-instructor-rev-votes', request).catch(error => {
                console.log(error)
            })
            return response.data
        },

        async getInstructorReviewTags(_, request) {
            let response = await axios.post('get-instructor-rev-tags', request).catch(error => {
                console.log(error)
            })
            return response.data
        }
    }
}