console.log("Script file loaded");
document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            const xhr = new XMLHttpRequest();
            xhr.open('POST', `/like/${postId}/`);
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    const likesCount = document.querySelector(`#post-${postId} .likes-count`);
                    likesCount.textContent = response.likes_count;
                    button.textContent = response.liked ? '좋아요 취소' : '좋아요';
                }
            };
            xhr.send();
        });
    });

    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const postId = this.dataset.postId;
            const content = this.querySelector('input[name="content"]').value;
            const xhr = new XMLHttpRequest();
            xhr.open('POST', `/comment/${postId}/`);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    const commentsDiv = document.querySelector(`#post-${postId} .comments`);
                    const newComment = document.createElement('div');
                    newComment.className = 'comment';
                    newComment.id = `comment-${response.comment_id}`;
                    newComment.innerHTML = `
                        <p>${response.username}: ${response.content}</p>
                        <button class="delete-comment-btn" data-comment-id="${response.comment_id}">삭제</button>
                    `;
                    commentsDiv.appendChild(newComment);
                    form.reset();
                }
            };
            xhr.send(`content=${encodeURIComponent(content)}`);
        });
    });

    document.addEventListener('click', function(e) {
        if (e.target && e.target.classList.contains('delete-comment-btn')) {
            const commentId = e.target.dataset.commentId;
            const xhr = new XMLHttpRequest();
            xhr.open('POST', `/comment/delete/${commentId}/`);
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    if (response.success) {
                        const commentDiv = document.querySelector(`#comment-${commentId}`);
                        commentDiv.remove();
                    }
                }
            };
            xhr.send();
        }
    });
});