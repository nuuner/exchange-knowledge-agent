# Exchange Knowledge Agent

An AI-powered agent that processes Microsoft Exchange emails to build and maintain a knowledge base. The agent automatically extracts, categorizes, and stores information from email communications.

## Current Status

🚧 **Work in Progress** - Basic structure and core components are being developed.

## Requirements

- Python 3.12+
- Microsoft Exchange Server access
- Valid Exchange credentials
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and configure your Exchange credentials
3. Install dependencies:
   ```bash
   uv install
   ```
4. Run the agent:
   ```bash
   uv run src/main.py
   ```

## What knowledge is being extracted?

- **People**
  - Contact details (email, phone, address)
  - Professional role (title, department, expertise)
  - Traits and preferences

- **Events**
  - Meetings (time, location, attendees, agenda)
  - Project milestones and deadlines
  - Key business activities

- **Organizations**
  - Company profile (name, industry, location)
  - Business relationships (clients, vendors, partners)
  - Key contacts and active projects

- **Documents**
  - Attachments and file metadata
  - *In the future*: Document processing (OCR, etc.)
    - Internal and external references
    - Process and technical documentation

## How can I view the knowledge base?

- The knowledge base is stored in a SQLite database. You can view it using a GUI like [DB Browser for SQLite](https://sqlitebrowser.org/) or use the database in your own applications.
  - **TODO**: A simple CLI interface for viewing the database
- In the future, I plan to add a more user-friendly interface for viewing and querying the knowledge base.

## Battleplan

- **Processing thread** listens for new emails and processes them
  - Remembers the date of the last processing
  - Only processes new emails since the last processing date
  - Peewee ORM for SQLite, used by the agent to store and query the knowledge base through the *Anthropic tools API* and used by the FastAPI thread to query the knowledge base.
- **FastAPI** thread for providing a simple API for anyone to query the knowledge base (This is not used by the agent itself, but by other applications/users)

### Tasks

1. Core Infrastructure
   - [ ] Set up Exchange email connection and authentication
   - [ ] Implement email polling/listening mechanism
   - [ ] Create SQLite database schema with Peewee ORM

2. Email Processing
   - [ ] Implement email content extraction
     - [ ] Sender, recipients
     - [ ] Subject, body
     - [ ] Attachments
     - [ ] Metadata
   - [ ] Simple model (No AI) for extracting all the information mentioned above
   - [ ] Implement last-processed-date tracking

3. Knowledge Extraction
   - [ ] Develop entity recognition for people, organizations, and events
   - [ ] Implement relationship mapping between entities
   - [ ] Create document metadata extraction
   - [ ] Set up attachment handling and storage

4. API Development
   - [ ] Set up FastAPI server structure
   - [ ] Create basic CRUD endpoints for knowledge base
   - [ ] Implement search and filtering capabilities

5. Future Enhancements
   - [ ] Implement attachment processing
   - [ ] Add web interface for knowledge base browsing
   - [ ] Create data visualization components
   - [ ] Develop export/import functionality

