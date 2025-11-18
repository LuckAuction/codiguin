CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL DEFAULT 'user', -- 'user' ou 'admin'
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela games (itens/keys)
CREATE TABLE games (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  platform TEXT,
  description TEXT,
  image TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela auctions
CREATE TABLE auctions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id INTEGER NOT NULL,
  start_price REAL NOT NULL,
  current_price REAL NOT NULL,
  start_time DATETIME NOT NULL,
  end_time DATETIME NOT NULL,
  seller_id INTEGER NOT NULL,
  status TEXT NOT NULL DEFAULT 'active', -- active, closed, canceled
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (game_id) REFERENCES games(id),
  FOREIGN KEY (seller_id) REFERENCES users(id)
);

-- Tabela bids
CREATE TABLE bids (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  auction_id INTEGER NOT NULL,
  bidder_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  placed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (auction_id) REFERENCES auctions(id),
  FOREIGN KEY (bidder_id) REFERENCES users(id)
);

-- Opcional: tabelas de pagamentos e chaves (keys)
CREATE TABLE keys (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  auction_id INTEGER NOT NULL,
  key_value TEXT,
  delivered BOOLEAN DEFAULT 0,
  FOREIGN KEY (auction_id) REFERENCES auctions(id)
);