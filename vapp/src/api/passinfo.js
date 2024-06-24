export function passInfo(method, path) {   //对对应路径的后端接口进行GET方法的封装函数
    let baseUrl = 'http://127.0.0.1:8000'; // Django 后端的地址

    if (method === 'GET') {
        // url为Django根端口+对应数据接口的path
        let url = `${baseUrl}${path}`;

        return fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();  // 解析 JSON 数据
        })
        .then(data => {
            return data;  // 返回解析后的数据
        });
    } else {
        throw new Error('Unsupported method');
    }
}
