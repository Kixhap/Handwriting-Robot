<h1>Handwriting
    App to translate text into handwriting with LLM integration.
<h2>How It Works</h2>
<ol>
    <li><strong>Input:</strong> The user asks a question to the LLM.</li>
    <li><strong>Response Generation:</strong> The LLM provides a textual response.</li>
    <li><strong>SVG Creation:</strong> The response is transformed into a vector graphic in SVG format, imitating handwritten text using <a href="https://github.com/sjvasquez/handwriting-synthesis">handwriting-synthesis</a>.</li>
    <li><strong>G-code Conversion:</strong> The generated SVG file is converted into G-code.</li>
    <li><strong>Robot Execution:</strong> The G-code can be used in robot control software such as <em>G-code sender</em> to reproduce the handwriting.</li>
</ol>

<h2>Features</h2>
<ul>
    <li>Automatic creation of handwritten notes</li>
</ul>

<h2>Requirements</h2>
    <ul>
        <li>Python environment</li>
        <li>Robot capable of interpreting G-code</li>
    </ul>

  <h2>Usage</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone &lt;repository_url&gt;
cd robot-control-program</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the program:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

  <h2>License</h2>
  <p>This project is licensed under the MIT License.</p>
