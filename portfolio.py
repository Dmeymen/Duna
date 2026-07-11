import streamlit as st
import datetime as date
import json

st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beige and white aesthetic with dark brown text
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        background: #42382B;
        color: #C5C3B9;
        font-family: Arial, monospace;
        line-height: 1.6;
    }

    .main {
        background-color: #42382B;
    }

    .navbar {
        background: linear-gradient(90deg, #42382B 0%, #771F02 100%);
        padding: 1rem 1rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
    }

    .hero-section {
        background: linear-gradient(135deg, #42382B 0%, #771F02 100%);
        padding: 2rem 1rem;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 3rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .hero-section h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #C5C3B9;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }

    .hero-section p {
        font-size: 1.3rem;
        opacity: 0.95;
        margin-bottom: 1.5rem;
    }

    .social-links {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
    }

    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem 1.5rem;
        background-color: #771F02;
        color: #C5C3B9;
        text-decoration: none;
        border-radius: 5px;
        transition: all 0.3s ease;
        border: 2px solid #771F02;
        font-weight: 500;
    }

    .social-btn:hover {
        background-color: #FC801D;
        border-color: #b88153;
        transform: translateY(-5px);
        box-shadow: 0 5px 15px #FC801D;
    }

    .section-title {
        color: #C5C3B9;
        font-size: 2rem;
        font-weight: 700;
        margin: 3rem 0 2rem 0;
        padding-bottom: 1rem;
        border-bottom: 3px solid #C5C3B9;
        display: inline-block;
    }

    .project-card {
        background: #42382B;
        border-radius: 10px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px #C5C3B9;
        transition: all 0.3s ease;
    }

    .project-card:hover {
        box-shadow: 0 8px 25px #C5C3B9;
        transform: translateY(-5px);
    }

    .project-card h3 {
        color: #C5C3B9;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .project-card .tags {
        margin-top: 1rem;
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .tag {
        background-color: #42382B;
        color: #C5C3B9;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }

    .skill-category {
        background-color: #42382B;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px #C5C3B9;
        border-top: 4px solid #771F02;
    }

    .skill-category h4 {
        color: #771F02;
        padding: 0.5rem 0.8rem;
        margin-bottom: 0.5rem;
        border-radius: 4px;
        font-size: 0.9rem;
    }

    .footer {
        background: linear-gradient(90deg, #42382B 0%, #771F02 100%);
        color: #C5C3B9;
        text-align: center;
        padding: 2rem;
        margin-top: 4rem;
        border-radius: 10px;
    }

    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #771F02, transparent);
        margin: 2rem 0;
    }

    .contact-box {
        background: #42382B;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 15px #C5C3B9;
        border-left: 5px solid #771F02;
        margin-top: 2rem;
    }

    .contact-box h3 {
        color: #C5C3B9;
        margin-bottom: 1rem;
    }

    .contact-item {
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
    }

    .contact-item strong {
        color: #C5C3B9;
        min-width: 100px;
    }

    html,
    body,
    .stApp,
    .main,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    [data-testid="stMain"],
    [data-testid="stVerticalBlock"] {
        background: #42382B !important;
        background-color: #42382B !important;
        color: #C5C3B9;
    }

    .navbar,
    .hero-section,
    .footer {
        background: linear-gradient(90deg, #42382B 0%, #771F02 100%) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    .section-title {
        color: #C5C3B9;
        border-bottom-color: #771F02;
    }

    .project-card,
    .skill-category,
    .contact-box {
        background: #42382B !important;
        color: #C5C3B9;
        box-shadow: 0 4px 15px rgba(96, 62, 38, 0.14);
        border-color: #771F02;
    }

    .project-card h3,
    .skill-category h4,
    .contact-box h3,
    .contact-item strong,
    .contact-item a {
        color: #C5C3B9;
    }

    .project-card p {
        color: #C5C3B9;
    }

    .tag {
        background-color: #42382B;
        color: #C5C3B9;
        border: 1px solid #771F02;
    }

    .skill-item {
        background-color: #771F02;
        color: #C5C3B9;
    }

    .divider {
        background: linear-gradient(90deg, transparent, #771F02, transparent);
    }

    /* Icon grid for languages & tools */
    .icon-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.2rem;
        margin: 1.5rem 0 2.5rem 0;
    }

    .icon-box {
        background-color: #42382B;
        border: 2px solid #771F02;
        border-radius: 8px;
        aspect-ratio: 1 / 1;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1.1rem;
        box-shadow: 0 4px 15px rgba(66, 56, 43, 0.25);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .icon-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(119, 31, 2, 0.35);
    }

    .icon-box img {
        width: 65%;
        height: 65%;
        object-fit: contain;
    }

    @media (max-width: 640px) {
        .icon-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    /* ---- Force dark text + terracotta glow everywhere, overriding Streamlit's own theme ---- */
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] strong,
    [data-testid="stMarkdownContainer"] a,
    [data-testid="stMarkdownContainer"] summary,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4 {
        color: #C5C3B9 !important;
        text-shadow: 0 0 4px rgba(119, 31, 2, 0.45), 0 0 1px rgba(119, 31, 2, 0.6);
    }

    /* Headings and project titles get a stronger glow to read as the "signature" elements */
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] summary {
        text-shadow: 0 0 8px rgba(119, 31, 2, 0.7), 0 0 2px rgba(119, 31, 2, 0.9);
    }

    /* Inline-colored spans (e.g. "Curious", "Skills") keep their own accent color, un-glowed-over */
    [data-testid="stMarkdownContainer"] span[style*="771F02"] {
        text-shadow: 0 0 6px rgba(119, 31, 2, 0.5);
    }

    /* st.info box: match the same dark-on-beige theme */
    [data-testid="stAlert"] {
        background-color: #42382B !important;
        border: 1px solid #771F02;
    }

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div {
        color: #C5C3B9 !important;
        text-shadow: 0 0 3px rgba(119, 31, 2, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# About section
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
        <p>
            <span style="font-weight:700; color: #771F02;">Curious</span> by nature.
            <span style="font-weight:700; color: #771F02;">Trained</span> in science.
            <span style="font-weight:700; color: #771F02;">Inspired</span> by art.
        </p>
        <p>
        Hi Everyone! I'm Duna Meya from Barcelona.
        I'm a junior engineer pursuing a bachelor's degree in AI & Data Science engineering
        at LaSalle Campus University Ramon Llull.
        </p>
        <p>Apart from coding, here are some activities that I love to do:</p>

        <style>
        .fancy-list {
            list-style: none;
            padding-left: 0;
            margin: 0;
        }
        .fancy-list li {
            position: relative;
            padding-left: 1.5rem;
            margin-bottom: 0.5rem;
            color: #C5C3B9;
        }
        .fancy-list li::before {
            content: "•";
            position: absolute;
            left: 0;
            top: 0;
            color: #C5C3B9;
            font-size: 1rem;
            line-height: 1;
            text-shadow: 0 0 4px #771F02;
        }
        </style>

        <ul class="fancy-list">
            <li>Travelling</li>
            <li>Sketching</li>
            <li>Graphic Design</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.info(
        "☕ **Location**: Barcelona, Spain\n\n"
        "🧋 **Education**: Bachelor's degree in AI & Data Science engineering at LaSalle Campus University Ramon Llull\n\n"
        "🧉 **Interest**: Sketching, Travelling, Graphic Design"
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<h2 class="section-title">Professional <span style="font-weight:700; color: #771F02;">Skills</span></h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="icon-grid">
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/c/c-original.svg" alt="C"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg" alt="Java"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" alt="MySQL"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python"></div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<h2 class="section-title"><span style="font-weight:700; color: #771F02;">Tools</span> I Use</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="icon-grid">
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/intellij/intellij-original.svg" alt="IntelliJ IDEA"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/clion/clion-original.svg" alt="CLion"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/datagrip/datagrip-original.svg" alt="DataGrip"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/webstorm/webstorm-original.svg" alt="WebStorm"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/PyCharm/PyCharm-original.svg" alt="PyCharm"></div>
        <div class="icon-box"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" alt="VS Code"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Project Section
st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "Creation of OS system - The Cytadel",
        "description": "A decentralized distributed application where independent nodes communicate, route data, and manage diplomacy and trade through concurrent processes without relying on a central server.",
        "details": '''
            <p><span style='font-weight:700; color: #771F02;'>Core Technologies:</span> C, POSIX Threads (pthreads), Sockets (TCP/IP), Binary I/O, IPC (Inter-Process Communication), Makefile, MD5 Verification.</p>

            <p>The Citadel System is a decentralized, multi-process distributed application designed to establish a network of communication, diplomacy, and trade between independent nodes (representing "Great Houses" or Realms). Operating without a centralized server, each independent node acts as a router capable of handling multihops, dynamically routing files and control data across a network topology based on localized configuration files.</p>

            <p>The primary architecture centers on a Maester (the main node process) and a pool of concurrent, decoupled Envoy assistant processes delegated to manage active network I/O operations without stalling system control.</p>

            <p><span style='font-weight:700; color: #771F02;'>Key Implementation Phases:</span></p>
            <ul class="fancy-list">
                <li>Node Control &amp; Interface: Engineered the Maester main process, incorporating custom binary file parsers for inventory management (stock.db) and a modular, non-blocking case-insensitive command terminal utilizing standard system I/O (read/write system calls only).</li>
                <li>Dynamic Multi-hop Routing &amp; Networking: Implemented standard network sockets to construct the peer-to-peer network matrix. Built an algorithmic routing subsystem that validates frame checksums and routes communications across neighbor nodes via configured or default paths.</li>
                <li>Robust Data &amp; File Transfer Protocol: Built a fragmented custom protocol to handle binary file transmission (for political alliance sigils and trade ledger transactions). Incorporated runtime integrity checking using md5sum process integration and precise byte padding.</li>
                <li>Internal Process Concurrency: Scaled the system to delegate dynamic networking pipelines concurrently. Implemented process forking (fork) and robust synchronization metrics to coordinate live communication pipelines between the main node and its array of Envoy subprocesses.</li>
            </ul>

            <p><span style='font-weight:700; color: #771F02;'>Core Technical Highlights &amp; Engineering Challenges:</span></p>
            <ul class="fancy-list">
                <li>Strict Low-Level Constraints: Developed entirely under strict system requirements prohibiting high-level library functions (such as printf, scanf, or standard wrapper libraries). All user terminal logs and file transfers were executed strictly via low-level read() and write() system calls to emphasize structural core system comprehension.</li>
                <li>Concurrency &amp; Coordination: Designed complex, multi-threaded inter-process synchronization structures to decouple asynchronous network wait-times from the responsive user shell interface.</li>
                <li>Fault Tolerance &amp; Reliability: Handled graceful structural exits, memory deallocation, and interrupt signals (CTRL+C). Managed communication edge cases including timeout drops, corrupt frame checksum validation, and node disconnect crash mitigations.</li>
            </ul>
        ''',
        "tags": ["C", "POSIX Threads", "IPC"],
        "link": "https://github.com/yourusername/the-cytadel"
    },
    {
        "title": "Object-Oriented Programming - Nude Eye Project",
        "description": "A personal portfolio website built using Streamlit to showcase my skills, projects, and contact information.",
        "details": '''
            <p><span style='font-weight:700; color: #771F02;'>Core Technologies:</span> Java, JSON, CSV, UML diagrams, Class diagrams, JavaDoc, File I/O, GRASP principles, layered architecture.</p>

            <p>The Nude Eye Project is a console-based marketplace for buying and selling eyewear, developed in Java as a Minimum Viable Product (MVP) for Phases 1 and 2. It allows users to register, log in, search products by name or supplier, view their profile with purchase history, and manage a shopping cart with checkout. Data persistence is handled via JSON files (products, suppliers, clients) and CSV files (sales history), with all information read from and written to disk on demand.</p>

            <p>Designed with object-oriented principles, the system follows a layered architecture (presentation, business logic, persistence) and applies key GRASP patterns, such as Information Expert, Controller, and Polymorphism, to ensure low coupling and high cohesion. This design also anticipates future extensions, like varying VAT calculations and new customer types, as outlined for Phases 3 and 4. The project is documented with UML class diagrams and JavaDoc, following a phased delivery schedule.</p>

            <p><span style='font-weight:700; color: #771F02;'>Key Implementation Phases:</span></p>
            <ul class="fancy-list">
                <li>(Design) Create a UML class diagram defining the core domain classes (Product, Supplier, Client, Sale, Cart) and their relationships, applying encapsulation and abstraction.</li>
                <li>(Implementation) Write the Java code based on the Phase 1 diagram. Implement console menus, JSON/CSV file I/O, and all MVP functionalities (registration, login, product search, profile, cart, checkout). Include JavaDoc documentation.</li>
                <li>(Design) Extend the class diagram to support new requirements: different product types, customer tiers (B2B, online), and flexible pricing/VAT rules. Apply inheritance and polymorphism to handle variations cleanly.</li>
                <li>(Implementation) Implement the extended design in Java, integrating the new features into the existing codebase.</li>
            </ul>

            <p><span style='font-weight:700; color: #771F02;'>Core Technical Highlights &amp; Engineering Challenges:</span></p>
            <ul class="fancy-list">
                <li>Object-oriented design: Full application of encapsulation, abstraction, inheritance, and polymorphism. Classes are designed with single responsibilities and clear boundaries between layers, following a layered architecture that separates Presentation (console menus), Business Logic (services), and Persistence (repositories) — ensuring low coupling and high cohesion.</li>
                <li>Data persistence: Dual-format storage — JSON for structured entities (products, suppliers, clients) and CSV for flat sales history. All data is read/written on demand, with no unnecessary in-memory caching. File validation uses startup checks that ensure critical files (products.json, providers.json) exist and are well-formed, with graceful degradation when optional files (clients.json, sales.csv) are missing — they are created on first use.</li>
                <li>Scalability for Phases 3 &amp; 4: New product types, customer roles, and pricing rules can be added without rewriting existing code, following the Open/Closed Principle — classes are open for extension (new subclasses) but closed for modification (existing code remains untouched), using interfaces and abstract classes liberally.</li>
            </ul>
        ''',
        "tags": ["Java", "JSON", "UML", "Layered Architecture"],
        "link": "#"
    },
    {
        "title": "Databases creation - Olympics Database",
        "description": "TODO: add a short description here.",
        "details": "TODO: add the full write-up here.",
        "tags": ["MySQL", "Data Cleaning", "Data Analysis"],
        "link": "#"
    }
]

for project in projects:
    tags_html = "".join([f'<span class="tag">{tech}</span>' for tech in project["tags"]])
    st.markdown(f"""
    <details class="project-card">
        <summary>{project['title']}</summary>
        <div class="project-details">
            <p>{project['description']}</p>
            <p>{project['details']}</p>
            <div class="tags">{tags_html}</div>
            <a href="{project['link']}" class="social-btn" target="_blank">View on GitHub</a>
        </div>
    </details>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)