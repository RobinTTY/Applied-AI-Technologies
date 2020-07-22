<template>
  <b-container id="main-content" class>
    <div id="loader-container">
      <div id="loader"></div>
    </div>
    <div id="swagger-editor"></div>
  </b-container>
</template>

<script src="https://editor.swagger.io/dist/swagger-editor-bundle.js"></script>
<script>
export default {
  mounted() {
    const setStyle = (selector, style, value) => {
      const element = document.querySelector(selector);
      const styleValue = `${style}:${value};`;

      if (!element) {
        console.error("Could not find an element for", selector);
        return;
      }

      if (document.all) {
        element.style.setAttribute("cssText", styleValue);
      } else {
        element.setAttribute("style", styleValue);
      }
    };

    window.editor = SwaggerEditorBundle({
      dom_id: "#swagger-editor",
      url:
        "https://raw.githubusercontent.com/RobinTTY/Applied-AI-Technologies/TeamB%40aai2020/doc/OpenApi/PostItRecognition.yaml"
    });

    // Hide the spinner
    setStyle("#loader-container", "display", "none");

    // Hide the editor parts
    setStyle("div.Pane.vertical.Pane1", "display", "none");
    setStyle("div.Pane.vertical.Pane2", "width", "100%");
    setStyle("div.SplitPane.vertical", "height", "100% !important");
    setStyle("section.container", "max-width", "100%");
    setStyle("div.Pane2", "overflow-y", "auto");

    window.addEventListener("dragstart", event => {
      event.preventDefault();
    });
  }
};
</script>

<style scoped>
#swagger-editor {
  margin-top: 3%;
  background: rgb(255, 255, 255, 0.7);
  border-radius: 15px;
}

#loader-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

#loader {
  border: 16px solid #f3f3f3;
  border-top: 16px solid #3498db;
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
