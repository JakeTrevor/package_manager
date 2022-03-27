"use strict";
function load_version(select, base_url) {
    console.log("loading version: " + select.value);
    let version_ID = select.value;
    let url = base_url + version_ID;
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
        let code_div = $("#code");
        let download_button = $("#download_version");
        let code_block;
        if (data.status === "OK") {
            code_block = "<pre><code>" + data.content + "</pre></code>";
            download_button.attr("href", data.download_url);
        }
        else {
            // this block should never run
            // but im not taking any chances
            code_block = data.content;
            download_button.removeAttribute("href");
        }
        code_div.html(code_block);
    })
        .then(() => {
        hljs.highlightAll();
    });
}
