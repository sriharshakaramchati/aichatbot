document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");
  const chatBox = document.getElementById("chat-box");
  const uploadForm = document.getElementById("upload-form");

  uploadForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    try {
      const response = await fetch("/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (data.success) {
        chatBox.innerHTML = "";
        uploadForm.reset();
        alert("Chat history uploaded successfully.");
      } else {
        alert("Failed to upload chat history.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to upload chat history.");
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const userMessage = chatInput.value.trim();

    if (!userMessage) {
      return;
    }

    chatBox.innerHTML += `<div class="message user-message">${userMessage}</div>`;
    chatInput.value = "";

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `message=${encodeURIComponent(userMessage)}`,
      });

      const data = await response.json();
      const botMessage = data.message;

      chatBox.innerHTML += `<div class="message bot-message">${botMessage}</div>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to send message.");
    }
  });
});
