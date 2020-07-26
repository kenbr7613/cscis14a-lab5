ALTER TABLE posts
ADD COLUMN createtime TIMESTAMP;
UPDATE posts SET createtime = NOW();
ALTER TABLE posts
ALTER COLUMN createtime SET DEFAULT NOW();
